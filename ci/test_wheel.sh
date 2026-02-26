set -e -x

if [[ "x${DSS_PYTHON_TEST_LINUX}" == "x1" ]]; then
    ORIGINAL_PATH=$PATH
    PYTHON_DIRS="cp311-cp311 cp312-cp312 cp313-cp313 cp314-cp314"
    for pydir in $PYTHON_DIRS
    do
        echo Installing for CPython $pydir
        export PATH=/opt/python/${pydir}/bin/:$ORIGINAL_PATH
        if [[ "x${SKIP_SCIPY}" != "x1" ]]; then
            python -m pip install scipy matplotlib
            python -m pip install artifacts/dss_python-*.whl
            python -c 'from dss import DSS; DSS.Plotting.enable(); DSS("new circuit.test123")'
        else
            python -m pip install artifacts/dss_python-*.whl
            python -c 'from dss import DSS; DSS("new circuit.test123")'
        fi
    done
else
    if [[ "x${SKIP_SCIPY}" != "x1" ]]; then
        python -m pip install scipy matplotlib
        python -m pip install artifacts/dss_python-*.whl
        python -c 'from dss import DSS; DSS.Plotting.enable(); DSS("new circuit.test123")'
    else
        python -m pip install artifacts/dss_python-*.whl
        python -c 'from dss import DSS; DSS("new circuit.test123")'
    fi
fi