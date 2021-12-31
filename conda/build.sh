BLD_PREV_DIR=`pwd`
echo "Building dss_python in $BLD_PREV_DIR"
rm -rf build dist .eggs
$PYTHON setup.py install --single-version-externally-managed --record=record.txt
