from __future__ import annotations
from typing import Optional
from ._cffi_api_util import CffiApiUtil
from .IDSS import IDSS
from enum import Flag

class OddieOptions(Flag):
    MapErrors = 0x01


class IOddieDSS(IDSS):
    r'''
    The OddieDSS class exposes the official OpenDSSDirect.DLL binary,
    as distributed by EPRI, with the same API as the DSS-Python and
    the official COM interface object on Windows. It uses AltDSS Oddie
    to achieve this.

    **Note:** This class requires the backend for Oddie to be included in
    the `dss_python_backend` package. If it is not available, an import 
    error should occur when trying to use this.

    AltDSS Oddie wraps OpenDSSDirect.DLL, providing a minimal compatiliby layer
    to expose it with the same API as AltDSS/DSS C-API. With it, we can
    just reuse most of the tools from the other projects on DSS-Extensions
    without too much extra work.

    Note that many functions from DSS-Extensions will not be available and/or
    will return errors, and this is expected. There are some issues and/or
    limitations from OpenDSSDirect.DLL that may or may not affect specific
    use cases; check the documentation on https://dss-extensions.org for 
    more information.

    :param library_path: The name or full path of the target dynamic library to
    load. Defaults to trying to load "OpenDSSDirect" from `c:\Program Files\OpenDSS\x64`,
    followed by trying to load it from the current path.

    :param load_flags: Optional, flags to feed the [`LoadLibrary`](https://learn.microsoft.com/en-us/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibraryexa) 
    (on Windows) or `dlopen` (on Linux and macOS, whenever EPRI supports it). If not provided, a default set will be used.

    :param oddie_options: Optional, Oddie configuration flags. If none passed,
    the default settings (recommended) will be used. For advanced users.
    '''

    def __init__(self, library_path: str = '', load_flags: Optional[int] = None, oddie_options: Optional[OddieOptions] = None):
        from dss_python_backend import _altdss_oddie_capi
        lib = _altdss_oddie_capi.lib
        ffi = _altdss_oddie_capi.ffi
        NULL = ffi.NULL
        
        c_load_flags = NULL
        if load_flags is not None:
            c_load_flags = ffi.new('uint32_t*', load_flags)

        if library_path:
            library_path = library_path.encode()
            lib.Oddie_SetLibOptions(library_path, c_load_flags)
            ctx = lib.ctx_New()
        else:
            # Try the default install folder
            library_path = rb'C:\Program Files\OpenDSS\x64\OpenDSSDirect.dll'
            lib.Oddie_SetLibOptions(library_path, c_load_flags)
            ctx = lib.ctx_New()
            if ctx == NULL:
                # Try from the general path, let the system resolve it
                library_path = rb'OpenDSSDirect.dll'
                lib.Oddie_SetLibOptions(library_path, c_load_flags)
                ctx = lib.ctx_New()

        if ctx == NULL:
            raise RuntimeError("Could not load the target library.")

        if lib.ctx_DSS_Start(ctx, 0) != 1:
            raise RuntimeError("DSS_Start call was not successful.")

        if oddie_options is not None:
            lib.Oddie_SetOptions(oddie_options)

        ctx = ffi.gc(ctx, lib.ctx_Dispose)
        api_util = CffiApiUtil(ffi, lib, ctx, is_odd=True)
        api_util._library_path = library_path
        IDSS.__init__(self, api_util)


__all__ = ['IOddieDSS', 'OddieOptions']