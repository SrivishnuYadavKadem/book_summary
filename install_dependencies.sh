#!/bin/bash
# Script to install all dependencies for the Book Summary application

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installing NLTK data..."
python -c "import nltk; nltk.download('stopwords')"

echo "Installation complete!"
echo "To run the application, use: python app.py"