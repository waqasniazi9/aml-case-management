@echo off
REM FIA AML Case Management System - Startup Script
REM This script starts the backend server

echo.
echo ========================================================
echo FIA AML Case Management System v3.0
echo ========================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Checking dependencies...
python -c "import flask, flask_cors, flask_sqlalchemy" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
)

echo.
echo Starting Backend Server...
echo.
echo Server will run on: http://localhost:5000
echo API Documentation: http://localhost:5000/api
echo.
echo Press Ctrl+C to stop the server
echo.

python aml_system.py

pause
