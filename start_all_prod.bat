@echo off
title YTLA Production Environment

echo.
echo ==============================
echo Starting YTLA Production Environment
echo ==============================
echo.

set "SCRIPT_DIR=%~dp0"

echo [1/2] Starting Backend Server...
start "Flask Backend [PROD]" cmd /k "%SCRIPT_DIR%start_backend_prod.bat"

echo Waiting for backend to start...
timeout /t 3 /nobreak >nul

echo [2/2] Starting Frontend Server...
start "Vue Frontend [PROD]" cmd /k "%SCRIPT_DIR%start_frontend_prod.bat"

echo.
echo ==============================
echo All servers started!
echo Backend: http://localhost:5000
echo Frontend: http://localhost:5173
echo ==============================

pause