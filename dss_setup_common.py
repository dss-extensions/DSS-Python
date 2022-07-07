import sys, os

# Not complete but should suffice for the moment
if 'linux' in sys.platform.lower():
    uname = os.uname()
    if uname.machine == 'aarch64':
        arch = 'arm64'
    elif uname.machine == 'x86_64':
        arch = 'x64'
    elif 'arm' in uname.machine:
        arch = 'arm32'
    else:
        arch = 'x86'
else:
    arch = 'x64' if (sys.maxsize > (1 << 32)) else 'x86'

if '-arm64' in os.environ.get('_PYTHON_HOST_PLATFORM', ''):
    arch = 'arm64'

platform_short = ''.join(filter(lambda ch: ch.isalpha(), sys.platform))
PLATFORM_FOLDER = '{}_{}'.format(platform_short, arch)

DSS_VERSIONS = ('v7', 'v7d')

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
