set -e -x
export PATH=/opt/python/cp39-cp39/bin/:$PATH
export DSS_PYTHON_MANYLINUX=1

cd dss_python
python3 -m pip install --upgrade pip cffi wheel
python3 setup.py --quiet bdist_wheel --py-limited-api cp36 --dist-dir="../artifacts_raw"
cd ..

# Bundle external shared libraries into the wheels
export LD_LIBRARY_PATH=${DSS_CAPI_PATH}/lib/linux_$1:$LD_LIBRARY_PATH
for whl in artifacts_raw/*.whl; do
    auditwheel repair "$whl" -w artifacts
done
