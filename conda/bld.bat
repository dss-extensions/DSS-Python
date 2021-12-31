REM Build dss_python
rd /s /q build 
rd /s /q dist
rd /s /q .eggs
"%PYTHON%" setup.py install --single-version-externally-managed --record=record.txt
if errorlevel 1 exit 1
