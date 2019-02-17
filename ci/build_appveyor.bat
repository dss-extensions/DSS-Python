SETLOCAL ENABLEEXTENSIONS

ren c:\cygwin cygwin.disabled

IF DEFINED APPVEYOR_REPO_TAG_NAME set APPVEYOR_REPO_TAG_NAME_DSS_PYTHON=%APPVEYOR_REPO_TAG_NAME%
set DSS_PYTHON_BUILD_TAG=0
IF DEFINED APPVEYOR_REPO_TAG_NAME set DSS_PYTHON_BUILD_TAG=1

set APPVEYOR_REPO_TAG_NAME=
setx DSS_PYTHON_BUILD_TAG %DSS_PYTHON_BUILD_TAG%

git clone --branch 0.10.1 https://github.com/dss-extensions/electricdss-src ../electricdss-src

git clone --branch 0.10.1 https://github.com/dss-extensions/dss_capi ../dss_capi

set originalpath=%path%

IF "%CONDA_SUBDIR%"=="win-32" SET MINICONDA_DIR=c:\miniconda3

IF "%CONDA_SUBDIR%"=="win-64" SET MINICONDA_DIR=c:\miniconda3-x64

set path=c:\cygwin64\bin;c:\cygwin64\usr\bin;c:\FPC\3.0.4\bin\i386-win32;c:\Program Files (x86)\Microsoft Visual Studio 14.0\vc\bin;%MINICONDA_DIR%;%MINICONDA_DIR%\scripts;%originalpath%

c:\cygwin64\bin\bash ci/build_windows.sh

echo POST c:\cygwin64\bin\bash ci/build_windows.sh

set path=c:\FPC\3.0.4\bin\i386-win32;c:\Program Files (x86)\Microsoft Visual Studio 14.0\vc\bin;%MINICONDA_DIR%;%MINICONDA_DIR%\scripts;%originalpath%

call %MINICONDA_DIR%\scripts\activate %MINICONDA_DIR%

echo POST ACTIVATE

echo DSS_PYTHON_BUILD_TAG=%DSS_PYTHON_BUILD_TAG%

IF "%DSS_PYTHON_BUILD_TAG%"=="1" conda-build --quiet --no-test --output-folder "c:\projects\artifacts" conda

echo CONDA-BUILD CALLED 

set path=c:\cygwin64\bin;c:\cygwin64\usr\bin;c:\FPC\3.0.4\bin\i386-win32;c:\Program Files (x86)\Microsoft Visual Studio 14.0\vc\bin;%MINICONDA_DIR%;%MINICONDA_DIR%\scripts;%originalpath%

c:\cygwin64\bin\bash ci/upload_windows.sh

dir ..\artifacts\*.whl ..\artifacts\*.tar.bz2 /s
