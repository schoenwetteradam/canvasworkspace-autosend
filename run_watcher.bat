@echo off
REM ===========================================================
REM  Starts the folder watcher. This is the one that runs all day.
REM  Task Scheduler can point at this file to launch it at login.
REM ===========================================================
cd /d "%~dp0"
python watcher.py
if errorlevel 1 (
  echo.
  echo  The watcher stopped with an error. See the message above.
  echo  Most often this means config.json is missing or not filled in.
  echo.
  pause
)
