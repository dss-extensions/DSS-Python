mkdir -p artifacts
cd dss_python
$PYTHON -m pip install --upgrade pip wheel hatch
$PYTHON -m pip install cffi
$PYTHON -m hatch build "$ARTIFACTS_FOLDER"
