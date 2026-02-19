## Project Structure
# PDF Accessible AI System

An AI-powered web application that converts non-accessible PDF documents into accessible, editable, and user-friendly HTML forms.  
The system uses OCR and intelligent field detection to preserve layout accuracy while enabling accessibility and form interaction.

---

## Problem Statement

Many PDFs are scanned or poorly structured, making them inaccessible to:
- Screen readers
- Keyboard-only navigation
- Users with disabilities

This project addresses the issue by automatically converting PDFs into accessible HTML forms while preserving the original layout.

---

## Features

- Upload scanned or non-accessible PDFs
- OCR-based text extraction
- Automatic form field detection
- Overlay editable fields on original PDF layout
- Signature support (draw or upload JPG)
- Feedback form handling
- Firebase authentication
- Save filled data back into a new PDF
- Accessibility-friendly HTML output

---

## Tech Stack

### Backend
- Python
- Flask
- Tesseract OCR
- OpenCV
- PDF processing libraries
- Firebase Admin SDK

### Frontend
- HTML
- CSS
- JavaScript
- Canvas API

---

## Project Structure

pdf-accessible-ai-system/
│
├── backend/
│ ├── core_pipeline/
│ │ ├── ai_pipeline.py
│ │ ├── field_extractor.py
│ │ ├── html_generator.py
│ │ ├── ocr_utils.py
│ │ ├── pdf_utils.py
│ │ └── run_pipeline.py
│ │
│ ├── routes/
│ │ ├── auth.py
│ │ ├── upload.py
│ │ └── feedback.py
│ │
│ ├── app.py
│ ├── firebase.py
│ ├── requirements.txt
│ └── test_firebase.py
│
├── frontend/
│ ├── css/
│ ├── js/
│ ├── pages/
│ └── index.html
│
├── Sample.pdf
├── README.md
└── .gitignore


---
## Installation and Setup

### Clone Repository
git clone https://github.com/Anjalee13625/pdf-accessible-ai-system.git
cd pdf-accessible-ai-system


## Backend Setup

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Firebase Setup
1)Create a Firebase project
2)Enable Email/Password Authentication
3)Download serviceAccountKey.json
4)Place it inside the backend/ folder
5)Do NOT upload this file to GitHub (ignored in .gitignore)

## Run the Application

python app.py

Open in browser:
http://localhost:5000

## Security Notes
1)serviceAccountKey.json is excluded using .gitignore
2)Virtual environments are not committed
3)Uploaded files are ignored from version control

## Use Cases
1)Accessible document generation
2)Assistive technology systems
3)Educational institutions
4)Government and public services

## Author
Anjalee
PDF Accessible AI System 

## License
This project is intended for educational and academic use.

