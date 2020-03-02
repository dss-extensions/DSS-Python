SETLOCAL ENABLEEXTENSIONS

ren c:\cygwin cygwin.disabled

IF DEFINED APPVEYOR_REPO_TAG_NAME set APPVEYOR_REPO_TAG_NAME_DSS_PYTHON=%APPVEYOR_REPO_TAG_NAME%
set DSS_PYTHON_BUILD_TAG=0
IF DEFINED APPVEYOR_REPO_TAG_NAME set DSS_PYTHON_BUILD_TAG=1

set APPVEYOR_REPO_TAG_NAME=
setx DSS_PYTHON_BUILD_TAG %DSS_PYTHON_BUILD_TAG%




set originalpath=%path%

IF "%CONDA_SUBDIR%"=="win-32" (
    SET MINICONDA_DIR=c:\miniconda3
    appveyor downloadfile https://github.com/dss-extensions/dss_capi/releases/download/%DSS_CAPI_TAG%/dss_capi_%DSS_CAPI_TAG%_win_x86.zip -FileName dss_capi.zip
)
IF "%CONDA_SUBDIR%"=="win-64" (
    SET MINICONDA_DIR=c:\miniconda3-x64
    appveyor downloadfile https://github.com/dss-extensions/dss_capi/releases/download/%DSS_CAPI_TAG%/dss_capi_%DSS_CAPI_TAG%_win_x64.zip -FileName dss_capi.zip
)
7z x -y -oC:\projects\ dss_capi.zip

set path=c:\cygwin64\bin;c:\cygwin64\usr\bin;c:\FPC\3.0.4\bin\i386-win32;c:\Program Files (x86)\Microsoft Visual Studio 14.0\vc\bin;%MINICONDA_DIR%;%MINICONDA_DIR%\scripts;%originalpath%

c:\cygwin64\bin\bash ci/build_windows.sh

echo POST c:\cygwin64\bin\bash ci/build_windows.sh

set path=c:\FPC\3.0.4\bin\i386-win32;c:\Program Files (x86)\Microsoft Visual Studio 14.0\vc\bin;%MINICONDA_DIR%;%MINICONDA_DIR%\scripts;%originalpath%

call %MINICONDA_DIR%\scripts\activate %MINICONDA_DIR%

echo POST ACTIVATE

echo DSS_PYTHON_BUILD_TAG=%DSS_PYTHON_BUILD_TAG%

REM IF "%DSS_PYTHON_BUILD_TAG%"=="1" conda-build --quiet --no-test --output-folder "c:\projects\artifacts" conda

REM echo CONDA-BUILD CALLED 

set path=c:\cygwin64\bin;c:\cygwin64\usr\bin;c:\FPC\3.0.4\bin\i386-win32;c:\Program Files (x86)\Microsoft Visual Studio 14.0\vc\bin;%MINICONDA_DIR%;%MINICONDA_DIR%\scripts;%originalpath%

c:\cygwin64\bin\bash ci/upload_windows.sh

dir ..\artifacts\*.whl ..\artifacts\*.tar.bz2 /s
