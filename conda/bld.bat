set BLD_PREV_DIR=%cd%
set BLD_PREV_PATH=%path%
set ELECTRICDSS_SRC_VERSION=0.9.8
set DSS_CAPI_VERSION=0.9.8

REM Clone dependency repositories
if not exist ..\electricdss-src (
    git clone -b "%ELECTRICDSS_SRC_VERSION%" --single-branch https://github.com/PMeira/electricdss-src.git ..\electricdss-src
    if errorlevel 1 exit 1
)

if not exist ..\dss_capi (
    git clone -b "%DSS_CAPI_VERSION%" --single-branch https://github.com/PMeira/dss_capi.git ..\dss_capi
    if errorlevel 1 exit 1
)

REM Build KLUSolve
cd ..\dss_capi
git clean -f -d
cd klusolve
rd /s /q build
mkdir build
cd build

cmake .. -DUSE_SYSTEM_SUITESPARSE=OFF -G "%CMAKE_GENERATOR%"
if errorlevel 1 exit 1

cmake --build . --config Release
if errorlevel 1 exit 1

REM Build dss_capi
cd ..\..
if "%target_platform%" == "win-32" (
    call build_win_x86.bat
    if errorlevel 1 exit 1
) else (
    call build_win_x64.bat
    if errorlevel 1 exit 1
)

set PATH=%BLD_PREV_PATH%

REM Finally build dss_python
cd %BLD_PREV_DIR%
"%PYTHON%" setup.py install --single-version-externally-managed --record=record.txt
if errorlevel 1 exit 1
