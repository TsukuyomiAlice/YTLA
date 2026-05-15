@echo off
title Build Frontend for Production

echo ==============================
echo Building Vue Frontend for Production...
echo ==============================

pushd "%~dp0ytla_plan_vue"

echo Current Directory: %cd%
echo.

echo Installing dependencies...
npm install

echo.
echo Building...
npm run build

echo.
echo Build completed! Output in dist/ directory.

popd
pause