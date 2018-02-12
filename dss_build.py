from cffi import FFI
import sys

ffi_builder_dss = FFI()
ffi_builder_dsspm = FFI()

with open('cffi/dss_capi_cffi.h', 'r') as f:
    cffi_header_dss = f.read()
    
with open('cffi/dsspm_capi_cffi.h', 'r') as f:
    cffi_header_dsspm = f.read()

with open('cffi/dss_capi_custom.c', 'r') as f:
    extra_source_dss = f.read()
    
ffi_builder_dss.cdef(cffi_header_dss)
ffi_builder_dsspm.cdef(cffi_header_dsspm)

extra = {}

# This ensures the shared libraries in the module directory can be
# loaded without changing LD_LIBRARY_PATH.
if sys.platform == 'linux':
    extra['extra_link_args'] = ["-Wl,-R,$ORIGIN/."]

ffi_builder_dss.set_source("_dss_capi", extra_source_dss,
    libraries=[r"dss_capi"],
    library_dirs=['../dss_capi/lib'],
    include_dirs=['../dss_capi/include'],
    source_extension='.c',
    **extra
)

ffi_builder_dsspm.set_source("_dsspm_capi", '#include <dsspm_capi.h>',
    libraries=[r"dsspm_capi"],
    library_dirs=['../dss_capi/lib'],
    include_dirs=['../dss_capi/include'],
    source_extension='.c',
    **extra
)

if __name__ == "__main__":
    ffi_builder_dss.compile(verbose=True)
    ffi_builder_dsspm.compile(verbose=True)
    