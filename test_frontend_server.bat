@echo off
title Test Frontend Server

echo ==============================
echo Testing Frontend Server Setup
echo ==============================
echo.

set "SCRIPT_DIR=%~dp0"
set "DIST_DIR=%SCRIPT_DIR%ytla_plan_vue\dist"

echo [1] Checking dist directory...
if exist "%DIST_DIR%" (
    echo OK: dist directory exists
) else (
    echo ERROR: dist directory not found!
    pause
    exit /b 1
)

echo.
echo [2] Checking index.html in dist...
if exist "%DIST_DIR%\index.html" (
    echo OK: index.html exists
    echo Content preview:
    type "%DIST_DIR%\index.html" | findstr "script"
) else (
    echo ERROR: index.html not found!
    pause
    exit /b 1
)

echo.
echo [3] Starting static server in dist directory...
pushd "%DIST_DIR%"
python "%SCRIPT_DIR%static_server.py" 5173

popd
pause