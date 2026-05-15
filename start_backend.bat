@echo off
title Flask Backend Server

echo ==============================
echo Starting Flask Backend Server...
echo ==============================

pushd "%~dp0ytla_plan"

echo Current Directory: %cd%
echo.

set PYTHONPATH=%~dp0
echo PYTHONPATH: %PYTHONPATH%
echo.

python app.py

popd
pause