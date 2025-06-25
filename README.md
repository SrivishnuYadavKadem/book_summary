# Book Summary Generator

A web application that generates summaries from PDF documents.

## Features

- Upload PDF documents
- Generate summaries of different lengths (short, medium, long)
- Extract keywords and topics
- Translate summaries to different languages
- Save and manage summaries

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/SrivishnuYadavKadem/book_summary.git
   cd book_summary
   ```

2. Create and activate a virtual environment (recommended):
   ```
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://localhost:5003
   ```

## How to Use

1. **Upload a PDF Document**:
   - Click the "Choose File" button
   - Select a PDF file from your computer
   - The file name will appear once selected

2. **Select Summary Options**:
   - Choose summary length:
     - Short: 25% of the original text
     - Medium: 50% of the original text
     - Long: 75% of the original text
   - Optionally select a target language for translation

3. **Generate Summary**:
   - Click the "Generate Summary" button
   - Wait for processing (larger documents take longer)

4. **View Results**:
   - Read the generated summary
   - See extracted keywords and topics
   - Check quality metrics

5. **Save Summary** (optional):
   - Click "Save Summary" to store it in the database
   - Access saved summaries from the list below

## Troubleshooting

- **PDF Not Loading**: Ensure the file is a valid PDF
- **Empty Summary**: Try a different summary length or check if the PDF contains extractable text
- **Translation Issues**: Check your internet connection as translation requires online API access
- **Database Errors**: Make sure the application has write permissions to the directory

## Project Structure

- `app.py`: Main Flask application
- `models/text_utils.py`: Text processing utilities
- `models/pdf_utils.py`: PDF processing utilities
- `static/`: CSS and JavaScript files
- `templates/`: HTML templates
- `uploads/`: Temporary storage for uploaded files

## License

MIT