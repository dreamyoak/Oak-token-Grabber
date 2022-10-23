@echo off
:fr
echo dont add spaces
set /p name="enter exe name : "
if [%name%] NEQ [] (
    pyinstaller --clean --onefile -i NONE --key OakGrabber -n %name% OakGrabber.py
    rmdir /s /q __pycache__
    rmdir /s /q build
    del /f / s /q %name%.spec
    echo exe Name: %name%.exe
    echo ur exe file generated in the dist folder
    pause
)
