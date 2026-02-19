# core_pipeline/pdf_utils.py
from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    images = convert_from_path(
        pdf_path,
        dpi=300
    )

    image_paths = []
    for i, img in enumerate(images):
        img_path = os.path.join(output_dir, f"page_{i+1}.png")
        img.save(img_path, "PNG")
        image_paths.append(img_path)

    return image_paths
