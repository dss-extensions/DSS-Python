from __future__ import print_function
from cffi import FFI
import sys
from dss_setup_common import PLATFORM_FOLDER, DSS_VERSIONS

extra = {}

# This ensures the shared libraries in the module directory can be
# loaded without changing LD_LIBRARY_PATH.
if sys.platform == 'linux':
    extra['extra_link_args'] = ["-Wl,-R,$ORIGIN/."]

ffi_builders = {}    
    
for version in DSS_VERSIONS:    
    ffi_builder_dss = FFI()

    with open('../dss_capi/include/{}/dss_capi.h'.format(version), 'r') as f:
        cffi_header_dss = f.read()
        cffi_header_dss = '\n'.join(
            line.replace('DSS_CAPI_{}_DLL'.format(version.upper()), '') for line in cffi_header_dss.split('\n') if not (
                line.strip().startswith('#') or 
                line.strip().startswith('extern "C"') or
                line.strip().endswith('extern "C"')
            )
        )
        
    with open('cffi/dss_capi_custom.h', 'r') as f:
        extra_header_dss = f.read()
        
    cffi_header_dss += extra_header_dss
    
    with open('cffi/dss_capi_custom.c', 'r') as f:
        extra_source_dss = f.read()
    
    ffi_builder_dss.cdef(cffi_header_dss)

    ffi_builder_dss.set_source("_dss_capi_{}".format(version), extra_source_dss,
        libraries=["dss_capi_{}".format(version)],
        library_dirs=['../dss_capi/lib/{}/{}'.format(PLATFORM_FOLDER, version)],
        include_dirs=['../dss_capi/include/{}'.format(version)],
        source_extension='.c',
        **extra
    )
    
    ffi_builders[version] = ffi_builder_dss

# Is there a better way to do this?
ffi_builder_v7 = ffi_builders['v7']
ffi_builder_v8 = ffi_builders['v8']
        
if __name__ == "__main__":
    for version, builder in ffi_builders.items():
        print('-' * 40)
        print('Building', version)
        print('-' * 40)
        builder.compile(verbose=True)
        print()
        
    
    