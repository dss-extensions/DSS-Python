set -e -x

cd ..

# Install Miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda.sh -q
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
conda config --set always_yes yes --set changeps1 no
conda install conda-build anaconda-client
conda update -q conda-build
#conda update -q conda
#conda info -a

mkdir ./artifacts
export ARTIFACTS_FOLDER=`python -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' ./artifacts`

cd dss_python

# conda-build with wheels doesn't seem consistent so
# we build the wheels manually
for PYVERSION in 2.7 3.5 3.6 3.7; do 
    echo Building for Python $PYVERSION...
    conda create -n py$PYVERSION python=$PYVERSION cffi
    source activate py$PYVERSION
    rm -rf .eggs
    rm -rf build
    python setup.py --quiet bdist_wheel --dist-dir="$ARTIFACTS_FOLDER"
done

# Build conda packages
# if [ -n "$TRAVIS_TAG_DSS_PYTHON" ]; then  # only run conda-build on tags, takes too long
#     conda-build --quiet --no-test --output-folder "$ARTIFACTS_FOLDER" conda 
# fi

# # Build wheels with conda
# # (if we keep the output section always, the default package
# # is ignored, uses wrong names, etc.)
# cat conda/meta_wheels.yaml >> conda/meta.yaml
# conda-build conda

# # undo the change, just in case
# git checkout conda/meta.yaml

# Upload artifacts to anaconda.org
if [ -n "$TRAVIS_TAG_DSS_PYTHON" ]; then
    if [ -n "$ANACONDA_API_TOKEN" ]; then 
        find ../artifacts -name "*.whl" -or -name "*.tar.bz2" | xargs -I {} anaconda upload --no-progress -l main -u pmeira {}
    fi
fi
