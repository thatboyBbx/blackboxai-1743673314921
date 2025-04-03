#!/bin/bash
echo "Installing Ministry Document Processor dependencies..."
pip install -r requirements.txt

echo "Downloading Tesseract OCR data..."
wget https://github.com/tesseract-ocr/tessdata/raw/main/eng.traineddata -P /usr/share/tesseract-ocr/4.00/tessdata/

echo "Setup complete. Core modules are ready for import."
echo "You can now integrate these into your VS Code interface:"
echo "- classifier.py for document classification"
echo "- ocr_utils.py for text extraction"