set BLD_PREV_DIR=%cd%
set BLD_PREV_PATH=%path%
set ELECTRICDSS_SRC_VERSION=0.10.2
set DSS_CAPI_VERSION=0.10.2

REM Clone dependency repositories
if not exist ..\electricdss-src (
    git clone -b "%ELECTRICDSS_SRC_VERSION%" --single-branch https://github.com/dss-extensions/electricdss-src.git ..\electricdss-src
    if errorlevel 1 exit 1
)

if not exist ..\dss_capi (
    git clone -b "%DSS_CAPI_VERSION%" --single-branch https://github.com/dss-extensions/dss_capi.git ..\dss_capi
    if errorlevel 1 exit 1
)

REM Build KLUSolve
if "%target_platform%" == "win-32" (
    SET CAPI_OUTPUT_FOLDER=win_x86
) else (
    SET CAPI_OUTPUT_FOLDER=win_x64
)
    
REM if not exist ..\dss_capi\%CAPI_OUTPUT_FOLDER%\libklusolve.dll (
cd ..\dss_capi
git clean -f -d
cd klusolve
rd /s /q build
mkdir build
cd build

set msvc2008=0
if "%CMAKE_GENERATOR%" == "Visual Studio 9 2008" set msvc2008=1
if "%CMAKE_GENERATOR%" == "Visual Studio 9 2008 Win64" set msvc2008=1

REM CMake doesn't know about Visual C++ 2008 for Python,
REM so we need to handle it manually
if "%msvc2008%" == "1" (
    if "%target_platform%" == "win-32" (
        call "C:\Program Files (x86)\Common Files\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat" x86
    ) else (
        call "C:\Program Files (x86)\Common Files\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat" x64
    )
    cmake .. -DUSE_SYSTEM_SUITESPARSE=OFF -G "NMake Makefiles" -DCMAKE_BUILD_TYPE=Release
) else (
    cmake .. -DUSE_SYSTEM_SUITESPARSE=OFF -G "%CMAKE_GENERATOR%" -DCMAKE_BUILD_TYPE=Release
    if errorlevel 1 exit 1
)

cmake --build . --config Release
if errorlevel 1 exit 1
REM )

REM Build dss_capi
cd ..\..
"c:\Program Files\Git\bin\bash" -c "bash ./make_metadata.sh"
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
rd /s /q build 
rd /s /q dist
rd /s /q .eggs
"%PYTHON%" setup.py install --single-version-externally-managed --record=record.txt
if errorlevel 1 exit 1
