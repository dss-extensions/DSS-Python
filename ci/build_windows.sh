set -e -x

APPVEYOR_REPO_TAG_NAME=

WGET=wget
ln -s /cygdrive/c /c

cd ..
export ARTIFACTS_FOLDER=`cygpath -a -w ./artifacts`

# Install Visual Studio Compiler for Python 2.7
#choco install -y vcpython27 
if [ ! -f "/c/projects/VCForPython27.msi" ]; then
    $WGET https://download.microsoft.com/download/7/9/6/796EF2E4-801B-4FC4-AB28-B59FBF6D907B/VCForPython27.msi -q -O /c/projects/VCForPython27.msi
fi
cd dss_python/ci
cmd "/c install_vcforpython27.bat"
# rm -rf /c/projects/VCForPython27.msi
cd ../..

export PATH="$PATH:/c/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin"

BUILD_WHEELS=1
if [ "$BUILD_WHEELS" == "1" ]; then
    # conda-build with wheels doesn't seem consistent so
    # we build the wheels manually
    if [[ -v APPVEYOR ]]; then 
        # Use the official Python already installed in AppVeyor
        cd dss_python

        # Python 27 is kept last since we rebuild klusolve for it
        if [ "$CONDA_SUBDIR" == "win-32" ]; then
            PYTHON_VERSIONS="35 36 37 38 27"
        else
            PYTHON_VERSIONS="35-x64 36-x64 37-x64 38-x64 27-x64"
        fi
        
        for A in $PYTHON_VERSIONS
        do
            echo Building for Python $A $CONDA_SUBDIR...
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

        PYTHON_VERSIONS="2.7 3.5 3.6 3.7 3.8"
        
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

# # Build conda packages
# export CONDA_SUBDIR=win-32
# conda-build --quiet --no-test --output-folder "$ARTIFACTS_FOLDER" conda
# export CONDA_SUBDIR=win-64
# conda-build --quiet --no-test --output-folder "$ARTIFACTS_FOLDER" conda

# # # Build wheels with conda
# # # (if we keep the output section always, the default package
# # # is ignored, uses wrong names, etc.)
# # rm -rf conda_wheels
# # cp -R conda conda_wheels
# # cat conda/meta_wheels.yaml >> conda_wheels/meta.yaml
# # export CONDA_SUBDIR=win-32
# # conda-build --output-folder ../artifacts conda_wheels
# # export CONDA_SUBDIR=win-64
# # conda-build --output-folder ../artifacts conda_wheels

# # # undo the change, just in case
# # git checkout conda/meta.yaml

# if [ -n "$ANACONDA_API_TOKEN" ]; then 
    # echo Upload artifacts to anaconda.org...
    # find ../artifacts -name "*.whl" -or -name "*.tar.bz2" | xargs -I {} anaconda upload --no-progress -l main -u pmeira {}
# fi
