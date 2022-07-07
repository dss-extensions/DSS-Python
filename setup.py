from setuptools import setup
import re, sys, shutil, os, io
import subprocess
from dss_setup_common import PLATFORM_FOLDER, DSS_VERSIONS, DLL_SUFFIX, DLL_PREFIX
import glob

MANYLINUX = os.environ.get('DSS_PYTHON_MANYLINUX', '0') == '1'

# Copy README.md contents
with io.open('README.md', encoding='utf8') as readme_md:
    long_description = readme_md.read()

# Handle the version string
# 1. Try env var DSS_PYTHON_VERSION
# 2. Try GITHUB_REF for a Git tag
# 3. Otherwise, just use the version the hardcoded version
package_version = os.environ.get('DSS_PYTHON_VERSION')
github_ref = os.environ.get('GITHUB_REF')
if package_version is None and github_ref is not None:
    package_version = github_ref[len("refs/tags/"):]

if package_version is not None:
    if re.match(r'^\d+\.\d+\.\d+(((a|b|(rc))\d*)|(\.dev\d+)){0,1}$', package_version) is None:
        package_version = None

if package_version is None:
    # Extract version from the source files
    with open('dss/__init__.py', 'r') as f:
        match = re.search("__version__ = '(.*?)'", f.read())
        package_version = match.group(1)
else:
    with open('dss/__init__.py', 'r') as f:
        init_py_orig = f.read()

    init_py = re.sub("__version__ = '(.*?)'", f"__version__ = '{package_version}'", init_py_orig)
    if init_py_orig != init_py:
        with open('dss/__init__.py', 'w') as f:
            f.write(init_py)

if os.environ.get('DSS_PYTHON_PREPARE_BOA') == '1':
    with open('conda/meta.yaml', 'r') as fin, open('conda/recipe.yaml', 'w') as fout:
        fout.write(fin.read().replace('{{ load_setup_py_data().version }}', package_version))

    exit()

# Copy all the DLLs from DSS C-API
src_path = os.environ.get('SRC_DIR', '')
DSS_CAPI_PATH = os.environ.get('DSS_CAPI_PATH', os.path.join(src_path, '..', 'dss_capi'))
base_dll_path_in = os.path.join(DSS_CAPI_PATH, 'lib', PLATFORM_FOLDER)
dll_path_out = os.path.abspath(os.path.join(src_path, 'dss'))
include_path_out = os.path.join(dll_path_out, 'include')

if not MANYLINUX:
    # for manylinux wheels, auditwheel handles copying the libs later
    for fn in glob.glob(os.path.join(base_dll_path_in, '*{}'.format(DLL_SUFFIX))):
        shutil.copy(fn, dll_path_out)

# Copy libs (easier to build custom extensions with a default DSS Python installation)
for fn in glob.glob(os.path.join(base_dll_path_in, '*.lib')) + glob.glob(os.path.join(base_dll_path_in, '*.a')):
    shutil.copy(fn, dll_path_out)

# Copy headers
if os.path.exists(include_path_out):
    shutil.rmtree(include_path_out)

shutil.copytree(os.path.join(DSS_CAPI_PATH, 'include'), include_path_out)

# Filter files to include in the Python package
extra_files = (
    glob.glob(os.path.join(include_path_out, '**', '*')) + 
    glob.glob(os.path.join(include_path_out, '*')) + 
    glob.glob(os.path.join(dll_path_out, '*.lib')) + 
    glob.glob(os.path.join(dll_path_out, '*.a'))
)

if MANYLINUX:
    # Do not pack .so files when building manylinux wheels
    # (auditwheel will copy and adjust them anyway)
    extra_args = dict(package_data={
        'dss': extra_files
    })
else:
    extra_args = dict(package_data={
        'dss': ['*{}'.format(DLL_SUFFIX)] + extra_files
    })

setup(
    name="dss_python",
    description="Python bindings and tools based on the DSS C-API project, a customized OpenDSS implementation",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Paulo Meira",
    author_email="pmeira@ieee.org",
    version=package_version,
    license="BSD",
    packages=['dss', 'dss.UserModels', 'dss.dss_capi_gr', 'dss.dss_capi_ir'],
    setup_requires=["cffi>=1.11.2"],
    cffi_modules=["dss_build.py:ffi_builder_{}".format(version) for version in DSS_VERSIONS] + 
        [
            'dss_build.py:ffi_builder_GenUserModel', 
            #'dss_build.py:ffi_builder_PVSystemUserModel', 
            #'dss_build.py:ffi_builder_StoreDynaModel', 
            #'dss_build.py:ffi_builder_StoreUserModel', 
            #'dss_build.py:ffi_builder_CapUserControl'
        ],
    ext_package="dss",
    install_requires=["cffi>=1.11.2", "numpy>=1.0"],
    tests_require=["zstandard", "scipy"],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License'
    ],
    **extra_args
)

