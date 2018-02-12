from setuptools import setup
import re, sys, shutil, os
import subprocess

# Convert README.md to RST for PyPi -- copied from (CC0) https://github.com/dhimmel/hetio
# Thank you, Daniel Himmelstein (dhimmel)!

# Try to create an rst long_description from README.md
try:
    args = 'pandoc', '--to', 'rst', 'README.md'
    long_description = subprocess.check_output(args)
    long_description = long_description.decode()
except Exception as error:
    print('README.md conversion to reStructuredText failed. Error:')
    print(error)
    print('Setting long_description to None.')
    long_description = None



with open('dss/__init__.py', 'r') as f:
    match = re.search("__version__ = '(.*?)'", f.read())
    version = match.group(1)


if sys.platform == 'win32':
    # Copy the DLLs on Windows
    base_dll_path_in = '../dss_capi/lib/'
    base_dll_path_out = 'dss'
    for fn in ('dss_capi.dll', 'dsspm_capi.dll', 'libklusolve.dll'):
        shutil.copy(
            os.path.join(base_dll_path_in, fn), 
            os.path.join(base_dll_path_out, fn)
        )
        
    extra_args = dict(package_data={
        'dss': ['*.dll']
    })
else:
    # Copy the DLLs on unix
    base_dll_path_in = '../dss_capi/lib/'
    base_dll_path_out = 'dss'
    for fn in ('libdss_capi.so', 'libdsspm_capi.so', 'libklusolve.so'):
        shutil.copy(
            os.path.join(base_dll_path_in, fn), 
            os.path.join(base_dll_path_out, fn)
        )
        
    extra_args = dict(package_data={
        'dss': ['*.so']
    })
    
setup(
    name="dss_python",
    description="OpenDSS bindings based on the DSS C-API project",
    author="Paulo Meira",
    author_email="pmeira@ieee.org",
    version=version,
    license="BSD",
    packages=['dss', 'dss.pm'],
    setup_requires=["cffi>=1.11.2"],
    cffi_modules=["dss_build.py:ffi_builder_dss", "dss_build.py:ffi_builder_dsspm"],
    ext_package="dss",
    install_requires=["cffi>=1.11.2", "numpy>=1.0"],
    zip_safe=False,
    long_description=long_description,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: SQL',
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License'
    ],
    **extra_args
)

