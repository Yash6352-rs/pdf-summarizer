from flask import Flask, render_template, request
import os
from summarizer import summarize_text  # make sure this is correctly imported
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = None
    if request.method == 'POST':
        if 'pdf' not in request.files:
            return "No file uploaded"

        file = request.files['pdf']
        if file.filename == '':
            return "No selected file"

        # Save PDF
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Extract text
        reader = PdfReader(filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        # Summarize
        summary = summarize_text(text)

    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
