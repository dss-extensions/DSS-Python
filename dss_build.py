from cffi import FFI
import sys, re, os
from dss_setup_common import PLATFORM_FOLDER, DSS_VERSIONS

def process_header(src, extern_py=False, implement_py=False, prefix='', v8=False):
    '''Prepare the DSS C-API headers for parsing and building with CFFI'''
    
    call_convention = '__stdcall ' if (sys.platform == 'win32') else ''
    
    src  = src.replace('dss_long_bool', 'int32_t')

    if not implement_py:
        src = re.sub('^extern .*', '', src, flags=re.MULTILINE)
        src = re.sub('^.*extern .*$', '', src, flags=re.MULTILINE)
        src = re.sub('^#.*', '', src, flags=re.MULTILINE)
        src = re.sub('DSS_CAPI_.*DLL', '', src)
        src = re.sub(
            r'DSS_MODEL_CALLBACK\(([^,]+), ([^\)]+)\)', 
            r'\1 ({call_convention}*\2)'.format(call_convention=call_convention), 
            src
        )
        if not v8:
            src = re.sub(r'.*/\*V8\*/', '', src)
    
    if extern_py:
        src = re.sub(
            r'DSS_MODEL_DLL\(([^\)]+)\) ', 
            r'extern "Python" \1 {prefix}'.format(prefix=prefix), 
            src
        )
        
    elif implement_py:
        # Extract the parameters from the definitions and implement a 
        # simple redirect to the Python-defined functions
        out_lines = []
        for line in src.split('\n'):
            if 'DSS_MODEL_DLL' not in line:
                out_lines.append(line)
                continue
        
            match = re.match(r'DSS_MODEL_DLL\((.*)\) (\w+)\((.*)\);', line)
            rtrn = 'return ' if match.group(1) != 'void' else ''
            name = match.group(2)
            if match.group(3) == 'void':
                params = []
            else:
                params = [
                    p.split(' ')[-1].strip('*') 
                    for p in match.group(3).split(',')
                ]
            
            out_lines.append(re.sub(
                r'DSS_MODEL_DLL\(([^\)]+)\) \w+\((.*)\);',
                r'''
static \1 {prefix}{name}(\2);
DSS_MODEL_DLL(\1) {name}(\2)
{{
    {rtrn}{prefix}{name}({params});
}}
'''.format(rtrn=rtrn, name=name, prefix=prefix, params=', '.join(params)), 
                line
            ))
            
        src = '\n'.join(out_lines)
    
    return src
    
extra = {}

# This ensures the shared libraries in the module directory can be
# loaded without changing LD_LIBRARY_PATH.
if sys.platform == 'linux':
    extra['extra_link_args'] = ["-Wl,-R,$ORIGIN/."]

ffi_builders = {}    

src_path = os.environ.get('SRC_DIR', '')
DSS_CAPI_PATH = os.environ.get('DSS_CAPI_PATH', os.path.join(src_path, '..', 'dss_capi'))
    
for version in DSS_VERSIONS:
    ffi_builder_dss = FFI()
    debug = 'd' if version.endswith('d') else ''

    with open(os.path.join(DSS_CAPI_PATH, 'include', 'dss_capi.h'), 'r') as f:
        cffi_header_dss = process_header(f.read())
        
    dss_capi_ctx_path = os.path.join(DSS_CAPI_PATH, 'include', 'dss_capi_ctx.h')
    if os.path.exists(dss_capi_ctx_path):
        with open(dss_capi_ctx_path, 'r') as f:
            cffi_header_dss += process_header(f.read())
        
    with open('cffi/dss_capi_custom.h', 'r') as f:
        extra_header_dss = f.read()
        
    cffi_header_dss += extra_header_dss
    
    with open('cffi/dss_capi_custom.c', 'r') as f:
        if os.path.exists(dss_capi_ctx_path):
            extra_source_dss = '#include <dss_capi_ctx.h>\n'
            extra_source_dss += f.read()
        else:
            extra_source_dss = f.read()
    
    ffi_builder_dss.cdef(cffi_header_dss)

    ffi_builder_dss.set_source("_dss_capi{}".format(debug), extra_source_dss,
        libraries=["dss_capi{}".format(debug)],
        library_dirs=[
            os.path.join(DSS_CAPI_PATH, 'lib/{}'.format(PLATFORM_FOLDER))
        ],
        include_dirs=[os.path.join(DSS_CAPI_PATH, 'include')],
        source_extension='.c',
        **extra
    )
    
    ffi_builders[version] = ffi_builder_dss


# User-model modules/DLLs
# Currently we build a separate DLL for each kind of model,
# since some functions are different. Some could probably be 
# merged in a single DLL, but there's not much benefit.

with open(os.path.join(DSS_CAPI_PATH, 'include/dss_UserModels.h'), 'r') as f:
    cffi_header_um = process_header(f.read())
    
user_models = [
    'GenUserModel',
    # 'PVSystemUserModel',
    # 'StoreDynaModel',
    # 'StoreUserModel',
    # 'CapUserControl',
]    

for user_model in user_models:    
    with open(os.path.join(DSS_CAPI_PATH, 'include', 'dss_{}.h'.format(user_model)), 'r') as f:
        func_def = f.read()
        
    prefix = "py{}_".format(user_model)
    user_model_def = process_header(func_def, extern_py=True, prefix=prefix)
    user_model_src = process_header(func_def, implement_py=True, prefix=prefix)
        
    ffi_builder = FFI()
    ffi_builder.cdef(cffi_header_um + user_model_def, packed=True)
    ffi_builder.set_source("_dss_{}".format(user_model), user_model_src,
        libraries=[],
        library_dirs=[],
        include_dirs=[os.path.join(DSS_CAPI_PATH, 'include')],
        source_extension='.c',
        #extra_compile_args=['/DYNAMICBASE:NO'],
        #extra_link_args=['/DYNAMICBASE:NO', '/NXCOMPAT:NO']
    )
    ffi_builders[user_model] = ffi_builder
        
# Is there a better way to do this? Unfortunately setup(cffi_modules=...)
# needs a list of strings and cannot handle objects directly
ffi_builder_v7 = ffi_builders['v7']
ffi_builder_v7d = ffi_builders['v7d']
# ffi_builder_v8 = ffi_builders['v8']
ffi_builder_GenUserModel = ffi_builders['GenUserModel']
#ffi_builder_PVSystemUserModel = ffi_builders['PVSystemUserModel']
#ffi_builder_StoreDynaModel = ffi_builders['StoreDynaModel']
#ffi_builder_StoreUserModel = ffi_builders['StoreUserModel']
#ffi_builder_CapUserControl = ffi_builders['CapUserControl']
        
if __name__ == "__main__":
    for version, builder in ffi_builders.items():
        print('-' * 40)
        print('Building', version)
        print('-' * 40)
        builder.compile(verbose=True)
        print()
