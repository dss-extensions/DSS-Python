mkdir -p artifacts
cd dss_python
$PYTHON -m pip install --upgrade pip wheel hatch
$PYTHON -m pip install cffi numpy pytest 'virtualenv<21' 
$PYTHON -m hatch build "$ARTIFACTS_FOLDER"
