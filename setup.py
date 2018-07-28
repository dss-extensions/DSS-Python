from setuptools import setup
import re, sys, shutil, os
import subprocess
from dss_setup_common import PLATFORM_FOLDER, DSS_VERSIONS, DLL_SUFFIX, DLL_PREFIX

with open('dss/v7/__init__.py', 'r') as f:
    match = re.search("__version__ = '(.*?)'", f.read())
    package_version = match.group(1)
    
# Copy the DLLs
for i, version in enumerate(DSS_VERSIONS):
    base_dll_path_in = '../dss_capi/lib/{}/{}'.format(PLATFORM_FOLDER, version)
    base_dll_path_out = 'dss/'
    
    file_list = ['dss_capi_{}'.format(version)]
    if i == 0:
        file_list.append('klusolve')
        
    for fn in file_list:
        shutil.copy(
            os.path.join(base_dll_path_in, DLL_PREFIX + fn + DLL_SUFFIX), 
            os.path.join(base_dll_path_out, DLL_PREFIX + fn + DLL_SUFFIX)
        )

        
extra_args = dict(package_data={
    'dss': ['*{}'.format(DLL_SUFFIX)]
})


setup(
    name="dss_python",
    description="OpenDSS bindings based on the DSS C-API project",
    author="Paulo Meira",
    author_email="pmeira@ieee.org",
    version=package_version,
    license="BSD",
    packages=['dss', 'dss.v7', 'dss.v8'],
    setup_requires=["cffi>=1.11.2"],
    cffi_modules=["dss_build.py:ffi_builder_{}".format(version) for version in DSS_VERSIONS],
    ext_package="dss",
    install_requires=["cffi>=1.11.2", "numpy>=1.0"],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: SQL',
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License'
    ],
    **extra_args
)

