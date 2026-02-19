# Accessible PDF Editor (AI-Based)

An AI-powered web application that converts non-accessible PDFs into fully editable and accessible PDF forms.

---

## Features

- Upload scanned or non-accessible PDFs
- OCR-based text extraction
- Auto-detection of form fields
- Editable accessible form generation
- Overlay form fields on original PDF layout
- Signature upload (JPG/PNG)
- Save filled data into a new PDF
- Firebase authentication (Login/Register)
- Accessible and clean UI

---

## Project Structure

PDF-Accessible-AI/
│
├── backend/
│ ├── app.py
│ ├── firebase.py
│ ├── requirements.txt
│ ├── serviceAccountKey.json
│ ├── core_pipeline/
│ │ ├── main.py
│ │ ├── pdf_utils.py
│ │ ├── ocr_utils.py
│ │ └── run_pipeline.py
│ └── static/
│ └── uploads/
│
├── frontend/
│ ├── css/
│ │ ├── base.css
│ │ └── editor.css
│ ├── js/
│ │ ├── auth.js
│ │ ├── upload.js
│ │ ├── editor.js
│ │ └── firebase.js
│ └── pages/
│ ├── index.html
│ ├── login.html
│ ├── register.html
│ ├── dashboard.html
│ ├── upload.html
│ ├── editor.html
│ └── feedback.html
│
├── Sample.pdf
└── README.md


---

## Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

Backend runs at:
http://127.0.0.1:8000

## Frontend Usage

Open the following file in a browser:

frontend/pages/index.html

---

## Firebase Setup

1.Create a Firebase project

2.Enable Email/Password authentication

3.Download serviceAccountKey.json

4.Place it inside the backend/ folder

## Sample PDF

A sample PDF is provided as Sample.pdf for testing upload and conversion.

## Technologies Used

1.Python

2.OCR (PDF Text Extraction)

3.HTML, CSS, JavaScript

4.Firebase Authentication

5.Canvas Overlay for PDF forms

## Author

Anjalee


