from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import os, shutil, json
from datetime import datetime

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- PATHS ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "core_pipeline", "output")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

FIELDS_PATH = os.path.join(OUTPUT_DIR, "fields.json")
FORM_HTML_PATH = os.path.join(OUTPUT_DIR, "ai_form.html")

# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {"status": "Backend running"}

# ---------------- UPLOAD ENDPOINT ----------------
@app.post("/api/upload")
async def upload_pdf(file: UploadFile = File(...)):
    pdf_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    run_ai_pipeline(pdf_path)

    return {"status": "processed", "file": file.filename}

# ---------------- GENERATED FORM ----------------
@app.get("/api/generated-form", response_class=HTMLResponse)
def get_generated_form():
    if not os.path.exists(FORM_HTML_PATH):
        return "<h3>No accessible form generated yet</h3>"

    with open(FORM_HTML_PATH, "r", encoding="utf-8") as f:
        return f.read()

# ---------------- AI PIPELINE (SIMULATION) ----------------
def run_ai_pipeline(pdf_path: str):
    print("🟢 Processing PDF:", pdf_path)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    fields = [
        {"label": "Name", "type": "text"},
        {"label": "Gender", "type": "radio", "options": ["Male", "Female", "Other"]},
        {"label": "Skills", "type": "checkbox", "options": ["Python", "ML", "Web"]},
        {"label": "Signature", "type": "text"}
    ]

    with open(FIELDS_PATH, "w", encoding="utf-8") as f:
        json.dump(fields, f, indent=2)

with open(FORM_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(f"""
    <div class="pdf-form">
      <h3>Accessible Form</h3>

      <label>Name</label>
      <input type="text" aria-label="Name"><br><br>

      <label>Gender</label><br>
      <input type="radio" name="gender"> Male
      <input type="radio" name="gender"> Female
      <input type="radio" name="gender"> Other<br><br>

      <label>Skills</label><br>
      <input type="checkbox"> Python
      <input type="checkbox"> ML
      <input type="checkbox"> Web<br><br>

      <label>Signature</label>
      <input type="text" aria-label="Signature"><br><br>
    </div>
    """)
    