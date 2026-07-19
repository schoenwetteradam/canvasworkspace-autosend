@echo off
REM ===========================================================
REM  First-time setup. Double-click this ONCE.
REM  Installs the Python packages and the browser the tool needs.
REM ===========================================================
setlocal
cd /d "%~dp0"

echo.
echo  Installing the tool's requirements. This can take a few minutes...
echo.

python -m pip install --upgrade pip
if errorlevel 1 goto :nopython

python -m pip install -r requirements.txt
if errorlevel 1 goto :failed

python -m playwright install chromium
if errorlevel 1 goto :failed

echo.
echo  ============================================
echo   Setup finished. You can close this window.
echo  ============================================
echo.
pause
exit /b 0

:nopython
echo.
echo  Could not find Python. Reinstall it from python.org and be sure
echo  to tick "Add python.exe to PATH" on the first install screen.
echo.
pause
exit /b 1

:failed
echo.
echo  Something went wrong during install. Check your internet connection
echo  and try running this file again.
echo.
pause
exit /b 1
