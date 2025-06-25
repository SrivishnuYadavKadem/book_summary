@echo off
REM Book Summary Generator Setup Script for Windows

echo Setting up Book Summary Generator...

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create uploads directory if it doesn't exist
echo Creating uploads directory...
if not exist uploads mkdir uploads

echo Setup complete! Run the application with:
echo call venv\Scripts\activate.bat ^&^& python app.py
echo Then open your browser to http://localhost:5003