@echo off
title Vue Frontend [PRODUCTION]

echo.
echo ==============================
echo Starting Vue Frontend Server
echo Mode: Production
echo ==============================
echo.

set "SCRIPT_DIR=%~dp0"

python "%SCRIPT_DIR%build_and_serve_frontend.py"

pause