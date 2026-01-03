@echo off
echo ==========================================
echo       Talvex One-Click Installer
echo ==========================================

echo [1/4] Creating Virtual Environment...
python -m venv .venv
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python not found. Please install Python 3.10+ and add to PATH.
    pause
    exit /b
)

echo [2/4] Activating Virtual Environment...
call .venv\Scripts\activate

echo [3/4] Installing Dependencies...
pip install -r requirements.txt

echo [4/4] Setting up Database and Admin...
python setup_app.py

echo ==========================================
echo       Setup Complete! Starting App...
echo ==========================================
start http://127.0.0.1:5000
python app.py
pause
