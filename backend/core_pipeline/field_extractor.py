import json
import os

KEYWORDS = {
    "name": "text",
    "email": "email",
    "phone": "tel",
    "address": "text",
    "date": "date",
    "dob": "date",
    "signature": "text"
}

def extract_fields(ocr_json_path, output_json_path):
    with open(ocr_json_path, "r", encoding="utf-8") as f:
        ocr_data = json.load(f)

    fields = []

    for item in ocr_data:
        text = item.get("text", "").lower()

        for key, field_type in KEYWORDS.items():
            if key in text:
                fields.append({
                    "label": item["text"],
                    "type": field_type,
                    "value": "",
                    "confidence": item.get("conf", 0)
                })

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(fields, f, indent=2)

    
