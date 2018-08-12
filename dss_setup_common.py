import sys

# Not complete but should suffice for the moment
arch = 'x64' if (sys.maxsize > (1 << 32)) else 'x86'
platform_short = ''.join(filter(lambda ch: ch.isalpha(), sys.platform))
PLATFORM_FOLDER = '{}_{}'.format(platform_short, arch)

DSS_VERSIONS = ('v7', 'v8')    

if sys.platform == 'win32':
    DLL_SUFFIX = '.dll'
    DLL_PREFIX = ''
elif sys.platform in ('linux', 'linux2'):
    DLL_SUFFIX = '.so'
    DLL_PREFIX = 'lib'
elif sys.platform == 'darwin':
    DLL_SUFFIX = '.dylib'
    DLL_PREFIX = 'lib'
else:
    raise RuntimeError("Unsupported platform!")
