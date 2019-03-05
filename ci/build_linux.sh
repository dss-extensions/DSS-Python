set -e -x

# Compile wheels
export DSS_PYTHON_MANYLINUX=1
cd /io/dss_python
for PYBIN in /opt/python/*/bin; do
    rm -rf /io/dss_python/.eggs/
    rm -rf /io/dss_python/build
    "${PYBIN}/python" setup.py --quiet bdist_wheel
done

# Bundle external shared libraries into the wheels
export LD_LIBRARY_PATH=/io/dss_python/dss:$LD_LIBRARY_PATH
for whl in dist/*.whl; do
    auditwheel repair "$whl" -w /io/artifacts
done
