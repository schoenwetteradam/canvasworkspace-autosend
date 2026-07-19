@echo off
REM ===========================================================
REM  Saves the CanvasWorkspace login once, so the watcher never
REM  has to log in again. Run this during setup, and again only
REM  if the saved session ever expires.
REM ===========================================================
cd /d "%~dp0"
python login_setup.py
if errorlevel 1 (
  echo.
  echo  Login setup stopped with an error. See the message above.
  echo.
)
pause
