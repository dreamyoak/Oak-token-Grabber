@echo off
:fr
echo dont add spaces
set /p name="enter exe name : "
if [%name%] NEQ [] (
    pyinstaller --clean --onefile --key OakGrabber -n %a% oakgrabber.py
    rmdir /s /q __pycache__
    rmdir /s /q build
    del /f / s /q %a%.spec
    echo exe Name: %name%.exe
    echo ur exe file generated in the dist folder
    pause
)
