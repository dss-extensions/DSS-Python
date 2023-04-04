set -e -x
export PATH=/opt/python/cp39-cp39/bin/:$PATH

cd dss_python
python3 -m pip install --upgrade pip wheel
python3 setup.py --quiet bdist_wheel --py-limited-api cp37 --dist-dir="../artifacts"
cd ..
