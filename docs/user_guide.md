# Ministry Document Processor - User Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Processing Documents](#processing-documents)
4. [Understanding Results](#understanding-results)
5. [Best Practices](#best-practices)
6. [Troubleshooting](#troubleshooting)

## Getting Started
### System Requirements
- Windows 10/11 or Linux
- 2GB RAM minimum
- 500MB disk space
- Tesseract OCR installed (included in installer)

### First Time Setup
1. Run `install.sh` (Linux/macOS) or `install.bat` (Windows)
2. Place the model file `naive_bayes_model.pkl` in the application folder
3. Launch with `python main.py`

## Interface Overview
**Main Components:**
1. **Document Drop Zone**: Central area for file input
2. **Process Button**: Starts document analysis
3. **Progress Bar**: Shows current operation status
4. **Results Panel**: Displays extracted text and classification
5. **Status Bar**: Shows system messages and errors

## Processing Workflow
1. **Add Documents**:
   - Drag files from Explorer/Finder into the drop zone
   - Or click the zone to browse files
   - Supported formats: PDF, PNG, JPG (max 20MB/file)

2. **Start Processing**:
   - Click "Process Documents" button
   - Progress bar will show completion status
   - Average processing time: 5-15 seconds per document

3. **Review Results**:
   - Classification appears first (category + confidence %)
   - Full extracted text follows
   - Processing time is displayed for each document

## Best Practices
- **For Best Accuracy**:
  - Use 300+ DPI scans
  - Ensure proper lighting and contrast
  - Avoid handwritten documents
  - Crop to content area when possible

- **For Performance**:
  - Process documents in batches of 10-20
  - Close other applications during large jobs
  - Restart application after processing 100+ documents

## Troubleshooting
**Common Issues:**
1. **"Model not found" error**:
   - Verify `naive_bayes_model.pkl` exists in the application folder
   - Check file permissions

2. **Poor OCR results**:
   - Rescan documents with better quality
   - Use the image preprocessing options
   - Check for smudges or stains on originals

3. **Slow performance**:
   - Reduce batch size
   - Lower image resolution (minimum 200 DPI)
   - Restart the application

## Support
For additional assistance:
- IT Helpdesk: helpdesk@ministry.gov
- Phone: x5555
- Hours: Mon-Fri 8am-5pm

Include the following in support requests:
1. Application version (shown in window title)
2. Screenshot of any error messages
3. Sample problematic documents (if applicable)