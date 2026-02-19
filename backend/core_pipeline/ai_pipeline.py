import subprocess
import sys
import os

def process_pdf(pdf_path):
    print("=== AI PIPELINE STARTED ===")
    print("PDF:", pdf_path)

    subprocess.run(
        [sys.executable, os.path.join("core_pipeline", "main.py"), pdf_path],
        check=True
    )
