@echo off
cd /d "%~dp0"
call venv\Scripts\activate
python -m waitress --port=8080 app:app
pause
