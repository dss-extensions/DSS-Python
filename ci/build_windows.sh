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

# Install the FreePascal compiler
if [ ! -f "/c/projects/FPC-win32-win64-3.0.4.7z" ]; then
    $WGET https://sourceforge.net/projects/dss-capi/files/FPC/FPC-win32-win64-3.0.4.7z/download -q -O /c/projects/FPC-win32-win64-3.0.4.7z
fi    
7z x -oC:/ c:/projects/FPC-win32-win64-3.0.4.7z
    
export PATH="$PATH:/c/FPC/3.0.4/bin/i386-win32"
export PATH="$PATH:/c/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin"


# Download SuiteSparse (once, otherwise the CMake script will download it multiple times)
if [ ! -f "/c/projects/SuiteSparse-5.3.0.tar.gz" ]; then
    $WGET http://faculty.cse.tamu.edu/davis/SuiteSparse/SuiteSparse-5.3.0.tar.gz -O /c/projects/SuiteSparse-5.3.0.tar.gz -q
fi
tar zxf /c/projects/SuiteSparse-5.3.0.tar.gz
export SUITESPARSE_SRC=`cygpath -a -w ./SuiteSparse`

BUILD_WHEELS=1
if [ "$BUILD_WHEELS" == "1" ]; then
    # Build KLUSolve
    if [ "$CONDA_SUBDIR" == "win-32" ]; then
        ## x86
        mkdir dss_capi/klusolve/build_x86
        cd dss_capi/klusolve/build_x86
        cmake .. -DUSE_SYSTEM_SUITESPARSE=OFF -G"Visual Studio 15 2017"
        cmake --build . --config Release
    else
        ## x64
        mkdir dss_capi/klusolve/build_x64
        cd dss_capi/klusolve/build_x64
        cmake .. -DUSE_SYSTEM_SUITESPARSE=OFF -G"Visual Studio 15 2017 Win64"
        cmake --build . --config Release
    fi


    # Build DSS C-API
    cd ../..
    bash ./make_metadata.sh
    if [ "$CONDA_SUBDIR" == "win-32" ]; then
        cmd "/c build_win_x86.bat"
    else
        cmd "/c build_win_x64.bat"
    fi
    
    cd ..


    # conda-build with wheels doesn't seem consistent so
    # we build the wheels manually
    if [[ -v APPVEYOR ]]; then 
        # Use the official Python already installed in AppVeyor
        cd dss_python

        # Python 27 is kept last since we rebuild klusolve for it
        if [ "$CONDA_SUBDIR" == "win-32" ]; then
            PYTHON_VERSIONS="35 36 37 27"
        else
            PYTHON_VERSIONS="35-x64 36-x64 37-x64 27-x64"
        fi
        
        for A in $PYTHON_VERSIONS
        do
            if [ "$A" == "27" ]; then
                OLD_DIR="`pwd`"
                cd ci
                cmd "/c build_klusolve_py27.bat"
                cd "$OLD_DIR"
            fi
        
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

        PYTHON_VERSIONS="2.7 3.5 3.6 3.7"
        
        for A in $PYTHON_VERSIONS
        do
            echo Building for Python $A $CONDA_SUBDIR...
            conda create -p ../py${A} python=$A cffi
            rm -rf .eggs build
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
