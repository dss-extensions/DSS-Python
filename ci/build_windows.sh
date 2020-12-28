set -e -x

APPVEYOR_REPO_TAG_NAME=

WGET=wget
ln -s /cygdrive/c /c

cd ..
export ARTIFACTS_FOLDER=`cygpath -a -w ./artifacts`

BUILD_WHEELS=1
if [ "$BUILD_WHEELS" == "1" ]; then
    # conda-build with wheels doesn't seem consistent so
    # we build the wheels manually
    if [[ -v APPVEYOR ]]; then 
        # Use the official Python already installed in AppVeyor
        cd dss_python

        if [ "$CONDA_SUBDIR" == "win-32" ]; then
            PYTHON_VERSIONS="39 38 35 36 37"
        else
            PYTHON_VERSIONS="39-x64 38-x64 35-x64 36-x64 37-x64"
        fi
        
        for A in $PYTHON_VERSIONS
        do
            echo Building for Python $A $CONDA_SUBDIR...
            c:/Python${A}/python -m pip install --upgrade pip
            c:/Python${A}/scripts/pip install cffi wheel
            rm -rf .eggs build
            c:/Python${A}/python setup.py --quiet bdist_wheel --dist-dir="$ARTIFACTS_FOLDER"
        done
        
        # Add Miniconda to PATH and install conda-build
        # export PATH="/c/miniconda3-x64:/c/miniconda3-x64/scripts:$PATH"
        conda config --set always_yes yes
        conda install conda-build anaconda-client
        # conda update -q conda-build
    else
        # Install Miniconda
        cd dss_python/ci
        $WGET https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -O Miniconda3.exe -q
        cmd "/c install_miniconda.bat"
        cd ..

        export PATH="/c/miniconda:/c/miniconda/scripts:$PATH"
        conda config --set always_yes yes
        conda install conda-build anaconda-client
        # conda update -q conda-build
        # conda update -q conda
        # conda info -a

        PYTHON_VERSIONS="3.5 3.6 3.7 3.8 3.9"
        
        for A in $PYTHON_VERSIONS
        do
            echo Building for Python $A $CONDA_SUBDIR...
            conda create -p ../py${A} python=$A cffi
            rm -rf .eggs build
            ../py$A/conda update -q setuptools pip wheel
            ../py$A/python setup.py --quiet bdist_wheel --dist-dir="$ARTIFACTS_FOLDER"
        done
    fi
else    
    if [[ -v APPVEYOR ]]; then 
        echo "Using Miniconda from AppVeyor"
        cd dss_python
    else
        # Install Miniconda
        echo "Installing Miniconda"
        cd dss_python/ci
        $WGET https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -O Miniconda3.exe -q
        cmd "/c install_miniconda.bat"
        cd ..

        export PATH="/c/miniconda:/c/miniconda/scripts:$PATH"
    fi
    conda config --set always_yes yes
    conda install conda-build anaconda-client
    # conda install -q conda-build=3.10.9
fi # BUILD_WHEELS

# Build conda packages
conda-build --quiet --no-test --output-folder "$ARTIFACTS_FOLDER" conda
