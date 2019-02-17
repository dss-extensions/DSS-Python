set -e -x

cd /io

if [ ! -f /io/dss_capi/lib/linux_x64/libklusolve.so ]; then
    export SUITESPARSE_SRC=`readlink -f ./SuiteSparse`

    # Build KLUSolve
    cd /io
    rm -rf dss_capi/klusolve/build
    ls -lR dss_capi/klusolve
    mkdir /io/dss_capi/klusolve/build
    ln -s SuiteSparse dss_capi/klusolve/build/
    cd /io/dss_capi/klusolve/build
    cmake -DUSE_SYSTEM_SUITESPARSE=OFF ..
    cmake --build . --config Release
fi

# Build DSS C-API
cd /io/dss_capi
bash make_metadata.sh
bash build_linux_x64.sh

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
