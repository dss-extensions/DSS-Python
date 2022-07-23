# Currently only for Linux

set -e -x

ORIGINAL_PATH=$PATH
PYTHON_DIRS="cp36-cp36m cp37-cp37m cp38-cp38 cp39-cp39 cp310-cp310 "

for pydir in $PYTHON_DIRS
do
    echo Installing for CPython $pydir
    export PATH=/opt/python/${pydir}/bin/:$ORIGINAL_PATH
    python -m pip install scipy matplotlib
    python -m pip install artifacts/dss_python-*.whl
    python -c 'from dss import DSS; DSS.Plotting.enable(); DSS("new circuit.test123")'
done
