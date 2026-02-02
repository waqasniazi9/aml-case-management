@echo off
REM ============================================
REM AML System - Public Online Access via ngrok
REM ============================================

echo.
echo ============================================
echo  Starting AML System Online Setup
echo ============================================
echo.

REM Kill any existing ngrok processes
taskkill /f /im ngrok.exe >nul 2>&1

REM Start the server
echo [1/3] Starting Flask server on port 5000...
timeout /t 2 >nul

REM Start ngrok
echo [2/3] Starting ngrok tunnel...
echo.
echo ============================================
echo  YOUR SYSTEM IS NOW ONLINE!
echo ============================================
echo.
echo ngrok is creating a public URL...
echo.

"C:\Users\OTS\AppData\Local\Programs\ngrok\ngrok.exe" http 5000

REM Show the ngrok web interface URL
echo.
echo For more details, visit:
echo http://localhost:4040
echo.
