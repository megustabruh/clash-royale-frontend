@echo off
REM Clash Royale Backend - Local Development Runner
REM Run this script to start the backend server locally

echo ======================================
echo Clash Royale Backend - Local Server
echo ======================================

cd /d "%~dp0"

REM Check if Python launcher is installed
py --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Install dependencies if needed
echo Installing dependencies...
py -m pip install -r requirements.txt -q

REM Run the server
echo Starting server at http://localhost:8002
echo API Docs: http://localhost:8002/docs
echo Press Ctrl+C to stop
echo ======================================
py -m uvicorn main_local:app --host 127.0.0.1 --port 8002

pause
