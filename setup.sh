#!/bin/bash

# Book Summary Generator Setup Script

echo "Setting up Book Summary Generator..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create uploads directory if it doesn't exist
echo "Creating uploads directory..."
mkdir -p uploads

echo "Setup complete! Run the application with:"
echo "source venv/bin/activate && python app.py"
echo "Then open your browser to http://localhost:5003"