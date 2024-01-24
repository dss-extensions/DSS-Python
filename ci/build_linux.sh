set -e -x
export PATH=/opt/python/cp39-cp39/bin/:$PATH

cd dss_python
python3 -m pip install --upgrade pip wheel hatch
python3 -m hatch build "../artifacts"
cd ..
