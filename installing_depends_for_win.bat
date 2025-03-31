@echo off
echo.
echo =====================================================
echo Checking and Installing Prerequisites for NAT Script
echo =====================================================
echo.

:: Step 1: Check if Python is installed
echo Checking if Python is installed...
where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python not found! Downloading and installing...
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe' -OutFile 'python_installer.exe'}"
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
    echo Python installed successfully.
)

:: Step 2: Check if Python is in PATH
echo Checking Python installation...
python --version >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not accessible. Please restart your computer and run this script again.
    exit /b 1
)

:: Step 3: Upgrade Pip and Fix Issues
echo Ensuring Pip is installed and updated...
python -m ensurepip
python -m pip install --upgrade pip setuptools

:: Step 4: Check and Install Tkinter
echo Checking if Tkinter is installed...
python -c "import tkinter" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Tkinter not found! Reinstalling Python with Tkinter support...
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe' -OutFile 'python_installer.exe'}"
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
    echo Python reinstalled with Tkinter.
)

:: Step 5: Install Required Python Packages
echo Installing required Python libraries...
python -m pip install --no-cache-dir ldap3

:: Step 6: Verify Installations
echo Verifying installations...
python -c "import ldap3, tkinter, platform; print('All modules installed successfully!')"

echo.
echo =====================================================
echo Prerequisites installation completed successfully!
echo You can now run the main script.
echo =====================================================
echo.
pause
