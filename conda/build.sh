BLD_PREV_DIR=`pwd`
BLD_PREV_PATH=$PATH

echo "Building in $BLD_PREV_DIR"

# Restore potential changes in PATH
export PATH=$BLD_PREV_PATH

# Finally build dss_python
echo "Building dss_python"
cd $BLD_PREV_DIR
rm -rf build dist .eggs
$PYTHON setup.py install --single-version-externally-managed --record=record.txt
