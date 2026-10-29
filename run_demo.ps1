# Accessible Banking - Team INNOVEX (DEXATHON 2026)
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "Accessible Banking for the Visually Impaired and Elderly" -ForegroundColor Yellow
Write-Host "Team: INNOVEX | Team ID: DEX26121 | Sathyabama Institute" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Cyan

Set-Location -Path $PSScriptRoot
Start-Process "http://localhost:5000"
python app.py
