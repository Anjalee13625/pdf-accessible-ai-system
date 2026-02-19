import pytesseract
from PIL import Image
import json
import os

def run_ocr(image_path, output_json):
    img = Image.open(image_path)

    data = pytesseract.image_to_data(
        img,
        output_type=pytesseract.Output.DICT
    )

    results = []

    for i in range(len(data["text"])):
        text = data["text"][i].strip()
        if text == "":
            continue

        x = data["left"][i]
        y = data["top"][i]
        w = data["width"][i]
        h = data["height"][i]

        results.append({
            "text": text,
            "bbox": [x, y, x + w, y + h]
        })

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return results
