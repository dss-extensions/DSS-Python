from setuptools import setup
import re, shutil, os, io
import glob

# Copy README.md contents
with io.open('README.md', encoding='utf8') as readme_md:
    long_description = readme_md.read()

# Handle the version string
# 1. Try env var DSS_PYTHON_VERSION
# 2. Try GITHUB_REF for a Git tag
# 3. Otherwise, just use the hardcoded version
package_version = os.environ.get('DSS_PYTHON_VERSION')
github_ref = os.environ.get('GITHUB_REF')
if package_version is None and github_ref is not None:
    package_version = github_ref[len("refs/tags/"):]

if package_version is not None:
    if re.match(r'^\d+\.\d+\.\d+((-\d+){0,1}|((a|b|(rc))\d*)|(\.dev\d+)){0,1}$', package_version) is None:        
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

# Copy all the i18n files
src_path = os.environ.get('SRC_DIR', '')
mo_path_out = os.path.abspath(os.path.join(src_path, 'dss', 'messages'))

# Filter files to include in the Python package
extra_files = (
    glob.glob(os.path.join(mo_path_out, '*.mo'))
)

extra_args = dict(package_data={
    'dss': extra_files
})

setup(
    name="dss_python",
    description="Python bindings and tools based on the DSS C-API project, the customized OpenDSS implementation from DSS-Extensions.org",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Paulo Meira",
    author_email="pmeira@ieee.org",
    version=package_version,
    license="BSD",
    packages=['dss', 'dss.UserModels'],
    ext_package="dss",
    install_requires=["dss_python_backend==0.13.1", "numpy>=1.19.5", "typing_extensions>=4.5,<5"],
    extras_require={'plot': ["matplotlib", "scipy"]}, #TODO: test which versions should work
    tests_require=["scipy", "ruff", "xmldiff", "pandas", "pytest"],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License'
    ],
    **extra_args
)

