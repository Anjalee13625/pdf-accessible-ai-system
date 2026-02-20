# 🚀 PDF Accessible AI System 

 AI-Powered PDF to Accessible HTML Conversion Platform  

 Python • Flask • OCR • Accessibility • Firebase  

📄 Upload PDFs • ♿ Accessibility • ✍️ Form Filling • 🧠 AI Processing

---

## 🎯 Overview

The **PDF Accessible AI System** is an AI-powered web application that converts **non-accessible or scanned PDF documents** into **accessible, editable, and user-friendly HTML forms**.

It is designed to support **users with disabilities**, particularly those relying on **screen readers, keyboard navigation, or assistive technologies**, by transforming static PDFs into interactive and accessible web formats.

This project is built for **academic demonstration** and **real-world accessibility use cases**.

---

## 🌟 Key Highlights

♿ **Accessibility First** – Screen-reader friendly HTML output  
🧠 **AI + OCR Powered** – Extracts text from scanned PDFs  
📝 **Editable Forms** – Detects and overlays form fields  
✍️ **Signature Support** – Draw or upload JPG signatures  
🎯 **Layout Preservation** – Maintains original PDF structure  
🔐 **Secure Backend** – Firebase authentication support  
🚀 **Demo Ready** – No complex setup for testing  

---

## 🚀 Quick Start

### Option 1: Manual Start (Recommended)

#### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## frontend
```bash
cd frontend
open index.html
```
🌐 Access Points

* Frontend UI: http://localhost:5000

* Backend API: http://localhost:5000/api

✨ Features

* 📄 PDF Upload & Processing

* Upload scanned or non-accessible PDF files

* Supports multi-page documents

* Secure file handling

🧠 OCR & AI Analysis

* OCR-based text extraction

* Intelligent form field detection

* Automatic label identification

📝 Accessible HTML Generation

* Converts PDFs into editable HTML forms

* Keyboard navigable elements

* Screen reader compatible structure

✍️ Signature Handling

* Auto-placement in signature fields

💬 Feedback & Data Capture

* User feedback input support

* Preserve filled data

* Export completed form back to PDF

🏗️ Architecture Overview
* User → PDF Upload → OCR Processing → Field Detection
     → HTML Form Generation → User Interaction
     → Data Capture → Accessible PDF Output

🛠️ Technology Stack
- Backend
  - Python
  - Flask
  - Tesseract OCR
  - OpenCV
  - PDF Processing Libraries
  - Firebase Admin SDK

- Frontend
  - HTML
  - CSS
  - JavaScript
  - Canvas API

```text
📁 Project Structure
pdf-accessible-ai-system/
│
├── backend/
│   ├── core_pipeline/
│   │   ├── ai_pipeline.py
│   │   ├── field_extractor.py
│   │   ├── html_generator.py
│   │   ├── ocr_utils.py
│   │   ├── pdf_utils.py
│   │   └── run_pipeline.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── upload.py
│   │   └── feedback.py
│   │
│   ├── app.py
│   ├── firebase.py
│   ├── requirements.txt
│   └── test_firebase.py
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── pages/
│   └── index.html
│
├── Sample.pdf
├── README.md
└── .gitignore
```
🔐 Security Notes

⚠️ Important

* serviceAccountKey.json is never uploaded

* Virtual environments are excluded

* Uploaded user files are ignored via .gitignore

* Example .gitignore entries:
```python
backend/venv/
__pycache__/
*.pyc
backend/static/uploads/*
serviceAccountKey.json
```

🎓 Academic & Professional Value
Learning Outcomes

* AI-based document processing

* OCR and NLP integration

* Accessibility-focused system design

* Full-stack web application

* Secure backend architecture

Use Cases

* Assistive technology platforms

* Government and public services

* Educational institutions

* Accessible form digitization

* Disability-inclusive systems

👩‍💻 Author

* Anjalee
* PDF Accessible AI System

📜 License

* This project is intended for educational and academic use only.
