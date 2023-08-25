@echo off
echo on
py -m venv venv
call venv\Scripts\activate.bat
py -m pip install --upgrade pip
pip install poetry
poetry install
uvicorn --host=0.0.0.0 --port=8002 app.main:app --reload