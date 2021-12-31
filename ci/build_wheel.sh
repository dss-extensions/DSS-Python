mkdir -p artifacts
cd dss_python
$PYTHON -m pip install --upgrade pip
$PYTHON -m pip install cffi wheel
$PYTHON setup.py --quiet bdist_wheel --py-limited-api cp36 --dist-dir=$ARTIFACTS_FOLDER
