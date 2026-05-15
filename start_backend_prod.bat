@echo off
title Flask Backend [PRODUCTION]

echo.
echo ==============================
echo Starting Flask Backend Server
echo Mode: Production
echo ==============================
echo.

set "SCRIPT_DIR=%~dp0"
set "BACKEND_DIR=%SCRIPT_DIR%ytla_plan"

pushd "%BACKEND_DIR%"

set PYTHONPATH=%SCRIPT_DIR%
set FLASK_ENV=production

echo [1/3] Checking Python environment...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    pause
    popd
    exit /b 1
)

echo [2/3] Checking waitress installation...
python -m pip show waitress >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing waitress...
    python -m pip install waitress
)

echo [3/3] Starting server...
echo PYTHONPATH: %PYTHONPATH%
echo FLASK_ENV: %FLASK_ENV%
echo.
python -m waitress --listen=0.0.0.0:5000 wsgi:app

popd