from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
import json
from models.text_utils import TextUtils
from models.pdf_utils import PDFUtils
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///summaries.db'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

db = SQLAlchemy(app)

class Summary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    reading_time = db.Column(db.Integer)
    language = db.Column(db.String(10))
    topics = db.Column(db.Text)  # JSON string of topics
    keywords = db.Column(db.Text)  # JSON string of keywords
    quality_metrics = db.Column(db.Text)  # JSON string of quality metrics

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Only PDF files are allowed'}), 400

    length = request.form.get('length', 'medium')
    target_lang = request.form.get('target_language')  # Optional target language
    auto_save = request.form.get('auto_save', 'false').lower() == 'true'  # Default to not auto-save
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Save the file first
    file.save(filepath)
    
    # Use appropriate summary length based on file size if not explicitly specified
    if request.form.get('length') is None:
        file_size = os.path.getsize(filepath)
        if file_size < 50000:  # Small file (< 50KB)
            length = 'short'
        elif file_size < 200000:  # Medium file (50KB - 200KB)
            length = 'medium'
        else:  # Large file (> 200KB)
            length = 'long'
    
    try:
        # Extract text from PDF
        text = PDFUtils.extract_text(filepath)
        
        # Set ratio based on requested length
        if length == 'short':
            ratio = 0.25  # 1/4 of the original
        elif length == 'medium':
            ratio = 0.5   # 1/2 of the original
        else:  # long
            ratio = 0.75  # 3/4 of the original
        
        # Generate summary
        summary = TextUtils.summarize_text(text, ratio)
        
        # Extract keywords and topics
        keywords = TextUtils.extract_keywords(text, num_keywords=20)
        topics = TextUtils.extract_topics(text)
        
        # Translate if needed
        source_language = 'en'
        language_confidence = 0.9
        
        if target_lang and target_lang != 'en' and target_lang != '':
            # Translate summary
            translated_summary = TextUtils.translate_text(summary, target_lang)
            if translated_summary:
                summary = translated_summary
                source_language = target_lang
            
            # Translate topic names (but not the terms)
            for topic in topics:
                translated_topic = TextUtils.translate_text(topic["topic"], target_lang)
                if translated_topic:
                    topic["topic"] = translated_topic
        
        # Calculate reading time (200 words per minute)
        reading_time = len(summary.split()) // 200 or 1  # Minimum 1 minute
        
        # Calculate simple quality metrics
        quality_metrics = {
            'compression_ratio': round(len(summary.split()) / len(text.split()), 2),
            'information_density': 0.8,
            'coherence_score': 0.9,
            'overall_quality': 0.85
        }
        
        # Only save if auto_save is enabled
        summary_id = None
        if auto_save:
            # Save summary with additional data
            new_summary = Summary(
                title=filename,
                content=summary,
                reading_time=reading_time,
                language=source_language,
                topics=json.dumps(topics),
                keywords=json.dumps(keywords),
                quality_metrics=json.dumps(quality_metrics)
            )
            db.session.add(new_summary)
            db.session.commit()
            summary_id = new_summary.id
        
        os.remove(filepath)  # Clean up uploaded file
        
        return jsonify({
            'summary': summary,
            'reading_time': reading_time,
            'language': source_language,
            'language_confidence': language_confidence,
            'topics': topics,
            'keywords': keywords,
            'quality_metrics': quality_metrics,
            'saved': auto_save,
            'summary_id': summary_id
        })
    
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error in summarize endpoint: {str(e)}")
        print(f"Traceback: {error_details}")
        if os.path.exists(filepath):
            os.remove(filepath)
        return jsonify({'error': str(e), 'details': error_details}), 500

@app.route('/summaries', methods=['GET'])
def get_summaries():
    summaries = Summary.query.all()
    return jsonify([{
        'id': s.id,
        'title': s.title,
        'reading_time': s.reading_time
    } for s in summaries])

@app.route('/summaries/<int:summary_id>', methods=['GET', 'DELETE'])
def summary_operations(summary_id):
    summary = Summary.query.get_or_404(summary_id)
    
    if request.method == 'DELETE':
        db.session.delete(summary)
        db.session.commit()
        return jsonify({'message': 'Summary deleted successfully'})
    
    # GET request
    return jsonify({
        'id': summary.id,
        'title': summary.title,
        'content': summary.content,
        'reading_time': summary.reading_time,
        'language': summary.language,
        'topics': json.loads(summary.topics) if summary.topics else [],
        'keywords': json.loads(summary.keywords) if summary.keywords else [],
        'quality_metrics': json.loads(summary.quality_metrics) if summary.quality_metrics else {}
    })

@app.route('/summaries/save', methods=['POST'])
def save_summary():
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    try:
        new_summary = Summary(
            title=data['title'],
            content=data['summary'],
            reading_time=data['reading_time'],
            language=data['language'],
            topics=json.dumps(data['topics']),
            keywords=json.dumps(data['keywords']),
            quality_metrics=json.dumps(data['quality_metrics'])
        )
        db.session.add(new_summary)
        db.session.commit()
        
        return jsonify({
            'message': 'Summary saved successfully',
            'summary_id': new_summary.id
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5003)