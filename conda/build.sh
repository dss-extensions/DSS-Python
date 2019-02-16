BLD_PREV_DIR=`pwd`
BLD_PREV_PATH=$PATH
ELECTRICDSS_SRC_VERSION=0.10.1
DSS_CAPI_VERSION=0.10.1

echo "Building in $BLD_PREV_DIR"

# If not found, download Free Pascal, install it in current user's home
echo "Checking for FPC..."
if [[ ! -x "`which fpc`" ]]; then
    echo "Downloading FPC..."
    export PATH=$PATH:~/fpc-3.0.4/bin
    if [[ ! -x "`which fpc`" ]]; then
        if [ `uname` == Linux ]; then
            wget https://sourceforge.net/projects/freepascal/files/Linux/3.0.4/fpc-3.0.4.x86_64-linux.tar/download -Ofpc.tar -q
            tar xf fpc.tar
            cd fpc-3.0.4.x86_64-linux
            echo > fpc_install_options.txt
            echo n >> fpc_install_options.txt
            echo n >> fpc_install_options.txt
            echo n >> fpc_install_options.txt
            echo "Installing FPC..."
            sh ./install.sh < fpc_install_options.txt
            cd ..
            rm -rf fpc-3.0.4.x86_64-linux
            export PATH=$PATH:~/fpc-3.0.4/bin
        fi
    fi
    if [ `uname` == Darwin ]; then
        wget https://sourceforge.net/projects/freepascal/files/Mac%20OS%20X/3.0.4/fpc-3.0.4.intel-macosx.dmg/download -Ofpc.dmg -q
        sudo hdiutil attach fpc.dmg
        sudo installer -package /Volumes/fpc-3.0.4.intel-macosx/fpc-3.0.4.intel-macosx.pkg -target /
    fi
fi

# Clone dependency repositories
echo "Cloning electricdss-src..."
if [ ! -d "../electricdss-src" ]; then
    git clone -b "$ELECTRICDSS_SRC_VERSION" --single-branch https://github.com/dss-extensions/electricdss-src.git ../electricdss-src
fi

echo "Cloning dss_capi..."
if [ ! -d "../dss_capi" ]; then
    git clone -b "$DSS_CAPI_VERSION" --single-branch https://github.com/dss-extensions/dss_capi.git ../dss_capi
fi

# Build KLUSolve
echo "Building KLUSolve"
cd ../dss_capi
git clean -f -d
cd klusolve
rm -rf build
mkdir build
cd build

cmake .. -DUSE_SYSTEM_SUITESPARSE=OFF -G "$CMAKE_GENERATOR" -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release
cd ../..


# Build dss_capi
bash make_metadata.sh
if [ `uname` == Linux ]; then
    bash build_linux_x64.sh
fi
if [ `uname` == Darwin ]; then
    bash build_macos_x64.sh
fi

# Restore potential changes in PATH
export PATH=$BLD_PREV_PATH

# Finally build dss_python
echo "Building dss_python"
cd $BLD_PREV_DIR
rm -rf build dist .eggs
$PYTHON setup.py install --single-version-externally-managed --record=record.txt
