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
   git clone <your-repository-url>
   cd book_summary
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:5003
   ```

## Usage

1. Upload a PDF document
2. Select summary length (short, medium, long)
3. Optionally select a target language
4. Click "Generate Summary"
5. View the summary, keywords, and topics
6. Save the summary if desired

## Project Structure

- `app.py`: Main Flask application
- `models/text_utils.py`: Text processing utilities
- `models/pdf_utils.py`: PDF processing utilities
- `static/`: CSS and JavaScript files
- `templates/`: HTML templates
- `uploads/`: Temporary storage for uploaded files

## License

MIT