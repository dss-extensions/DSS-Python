import sys

# Not complete but should suffice for the moment
arch = 'x64' if (sys.maxsize > (1 << 32)) else 'x86'
platform_short = ''.join(filter(lambda ch: ch.isalpha(), sys.platform))
PLATFORM_FOLDER = '{}_{}'.format(platform_short, arch)

DSS_VERSIONS = ('v7', 'v8')    

if sys.platform == 'win32':
    DLL_SUFFIX = '.dll'
elif sys.platform == 'linux':
    DLL_SUFFIX = '.so'
elif sys.platform == 'darwin':
    DLL_SUFFIX = '.dylib'
else:
    raise RuntimeError("Unsupported platform!")
