# Test Documents Directory

## Directory Structure
```
data/test_documents/
├── applications/
│   ├── residency_application_2023-01.pdf
│   └── permit_application_2023-02.jpg
├── reports/
│   ├── monthly_report_2023-03.pdf
│   └── annual_report_2023-04.png
├── complaints/
│   ├── service_complaint_2023-05.pdf
│   └── facility_complaint_2023-06.jpg
└── sample_batch/
    ├── mixed_documents_01.pdf
    └── mixed_documents_02.pdf
```

## Recommended Test Files
1. **By Category** (5-10 samples each):
   - Applications (PDF, JPG)
   - Reports (PDF, PNG)
   - Complaints (PDF, JPG)
   - Permits (PDF)
   - Invoices (JPG, PNG)

2. **By Quality** (per category):
   - 60% Good quality (clear text, proper alignment)
   - 30% Medium quality (slightly blurred, minor skew)
   - 10% Poor quality (heavy skew, low contrast)

3. **By Length**:
   - 70% 1-3 pages
   - 20% 4-5 pages
   - 10% 6+ pages (stress test)

## File Naming Convention
`[category]_[description]_[date].[ext]`  
Examples:
- `application_visa_2023-01-15.pdf`
- `report_monthly_2023-02-28.png`
- `complaint_noise_2023-03-10.jpg`

## Test Scenarios
1. **Basic Validation**:
   - Single document processing
   - Verify classification accuracy
   - Check text extraction quality

2. **Batch Processing**:
   - 10-20 documents at once
   - Monitor memory usage
   - Verify consistent performance

3. **Edge Cases**:
   - Password-protected PDFs (should fail gracefully)
   - Corrupted files (should handle errors)
   - Extremely large files (>20MB)

## Notes
- Use representative samples of actual ministry documents
- Remove or redact sensitive information before testing
- Maintain variety in document layouts and formats
- Include some multi-language documents if applicable