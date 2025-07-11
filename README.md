# 📄 PDF Summarizer

**PDF Summarizer** is a lightweight, responsive web application that allows users to upload a PDF file and receive a concise, AI-generated summary using Google’s Gemini API.

It’s perfect for students, professionals, and researchers who want to extract key points from lengthy documents—saving time and boosting productivity.

---

## Features

- Upload a PDF (any length)  
- Automatically generate a short, easy-to-read summary  
- Clean and friendly interface  
- Option to download the summary as a `.txt` file  
- Loading spinner while the AI processes your file  
- Secure API integration via `.env` file

---

## Screenshots


---

## Project Structure

- app.py # Flask app setup and routes
- summarizer.py # Handles text extraction and Gemini summarization
- templates/
  - index.html # HTML front-end
- static/
  - style.css # CSS styling
- uploads/ # Temporary storage for uploaded PDFs
- .env # Your API key
- .gitignore # Files/folders to ignore in Git
- README.md

---

## ⚙Setup Instructions

### 1. Clone the Repository

- git clone https://github.com/Yash6352-rs/pdf-summarizer.git
- cd pdf-summarizer

### 2. Create Virtual Environment (optional but recommended)

This or use anaconda prompt
- python -m venv venv
- source venv/bin/activate

### 3. Install Requirements

pip install Flask PyPDF2 python-dotenv google-generativeai

### 4. Setup Gemini API Key

Create a .env file in the root directory:
-GEMINI_API_KEY=your_google_gemini_api_key

## Running the App

python app.py

---

## Usage Instructions

1. Upload a .pdf file using the form
2. Click “Summarize PDF”
3. Wait a few seconds (spinner shows progress)
4. View your summary
5. Click “Download Summary” to save it as .txt
