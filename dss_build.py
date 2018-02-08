from cffi import FFI
import sys

ffi_builder = FFI()

with open('cffi/dss_capi_cffi.h', 'r') as f:
    cffi_header = f.read()

with open('cffi/dss_capi_custom.c', 'r') as f:
    extra_source = f.read()
    
ffi_builder.cdef(cffi_header)

extra = {}

# This ensures the shared libraries in the module directory can be
# loaded without changing LD_LIBRARY_PATH.
if sys.platform == 'linux':
    extra['extra_link_args'] = ["-Wl,-R,$ORIGIN/."]

ffi_builder.set_source("_dss_capi", extra_source,
    libraries=[r"dss_capi"],
    library_dirs=['../dss_capi/lib'],
    include_dirs=['../dss_capi/include'],
    source_extension='.c',
    **extra
)

if __name__ == "__main__":
    ffi_builder.compile(verbose=True)
    