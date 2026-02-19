import os
from pdf_utils import pdf_to_images
from ocr_utils import run_ocr
from field_extractor import extract_fields
from html_generator import generate_html_form



PDF_PATH = "sample.pdf"
IMAGE_DIR = "core_pipeline/output/images"
OCR_DIR = "core_pipeline/output/ocr"
FIELDS_JSON = "core_pipeline/output/fields.json"
HTML_FORM = "core_pipeline/output/ai_form.html"

os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(OCR_DIR, exist_ok=True)

# STEP 1 — PDF → Images
images = pdf_to_images(PDF_PATH, IMAGE_DIR)

# STEP 2 — OCR
for img_path in images:
    page_name = os.path.splitext(os.path.basename(img_path))[0]
    out_json = os.path.join(OCR_DIR, f"{page_name}_ocr.json")
    run_ocr(img_path, out_json)

# STEP 3 — Field Extraction
ocr_json = os.path.join(OCR_DIR, "page_1_ocr.json")
extract_fields(ocr_json, FIELDS_JSON)

# STEP 4 — HTML Form Generation
generate_html_form(FIELDS_JSON, HTML_FORM)
