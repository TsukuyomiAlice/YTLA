@echo off
title Vue Frontend Server

echo ==============================
echo Starting Vue Frontend Server...
echo ==============================

pushd "%~dp0ytla_plan_vue"

echo Current Directory: %cd%
echo.

npm run dev

popd
pause