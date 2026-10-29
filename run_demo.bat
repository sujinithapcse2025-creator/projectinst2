@echo off
title Accessible Banking - Team INNOVEX (DEXATHON 2026)
echo ======================================================================
echo Accessible Banking for the Visually Impaired and Elderly
echo Team: INNOVEX ^| Team ID: DEX26121 ^| Sathyabama Institute
echo ======================================================================
echo.
cd /d "%~dp0"

echo [1/2] Starting Flask Mock Banking Server...
start "INNOVEX Banking Server" python app.py

echo [2/2] Waiting 2 seconds for server to initialize...
timeout /t 2 /nobreak >nul

echo Opening browser at http://localhost:5000 ...
start http://localhost:5000

echo.
echo Server is running! Keep this window open during demo.
echo To stop the server, simply close the server window.
