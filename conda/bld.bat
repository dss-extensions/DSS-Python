set BLD_PREV_DIR=%cd%
set BLD_PREV_PATH=%path%

REM Finally build dss_python
cd %BLD_PREV_DIR%
rd /s /q build 
rd /s /q dist
rd /s /q .eggs
"%PYTHON%" setup.py install --single-version-externally-managed --record=record.txt
if errorlevel 1 exit 1
