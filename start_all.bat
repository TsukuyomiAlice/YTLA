@echo off
title Start All Servers

echo ==============================
echo Starting All Servers...
echo ==============================

echo Starting Flask Backend Server...
start "Flask Backend" cmd /k "%~dp0start_backend.bat"

timeout /t 3 /nobreak > nul

echo Starting Vue Frontend Server...
start "Vue Frontend" cmd /k "%~dp0start_frontend.bat"

echo.
echo Servers started successfully!
echo - Backend: http://localhost:5000
echo - Frontend: http://localhost:5173
echo.

pause