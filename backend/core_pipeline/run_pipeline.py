import json
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

def run_pipeline(pdf_path):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ⚠️ SIMULATION (replace with real AI later)
    fields = [
        {"label": "Name", "type": "text"},
        {"label": "Signature", "type": "text"},
        {"label": "Gender", "type": "radio", "options": ["Male", "Female"]}
    ]

    # Save fields.json
    with open(os.path.join(OUTPUT_DIR, "fields.json"), "w", encoding="utf-8") as f:
        json.dump(fields, f, indent=2)

    # Generate accessible HTML
    html = "<form aria-label='Accessible PDF Form'>"
    for field in fields:
        html += f"<label>{field['label']}</label><br>"
        if field["type"] == "text":
            html += "<input type='text'><br><br>"
        elif field["type"] == "radio":
            for opt in field["options"]:
                html += f"<input type='radio' name='{field['label']}'>{opt}<br>"
            html += "<br>"
    html += "</form>"

    with open(os.path.join(OUTPUT_DIR, "ai_form.html"), "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ AI pipeline ran for:", pdf_path)
