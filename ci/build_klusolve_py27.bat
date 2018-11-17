REM Build KLUSolve
cd ..\..
rd /s /q dss_capi\klusolve\build_x86
rd /s /q dss_capi\klusolve\build_x64
mkdir dss_capi\klusolve\build_x86
mkdir dss_capi\klusolve\build_x64

REM x86
cd dss_capi\klusolve\build_x86
call "C:\Program Files (x86)\Common Files\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat" x86
cmake .. -DUSE_SYSTEM_SUITESPARSE=OFF -G "NMake Makefiles" -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release

REM x64
cd dss_capi\klusolve\build_x64
call "C:\Program Files (x86)\Common Files\Microsoft\Visual C++ for Python\9.0\vcvarsall.bat" x64
cmake .. -DUSE_SYSTEM_SUITESPARSE=OFF -G "NMake Makefiles" -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release

