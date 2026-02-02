# 🔌 AI Assessment API - Technical Documentation

## Classes Overview

### 1. DocumentProcessor

Handles all document text extraction with automatic file type detection.

#### Methods

##### `extract_text_from_image(filepath)`

- **Input**: Path to image file (JPG, PNG, GIF, etc.)
- **Output**: Extracted text string
- **Technology**: OCR (Tesseract via pytesseract)
- **Error Handling**: Returns "[Image - no readable text]" on failure

##### `extract_text_from_pdf(filepath)`

- **Input**: Path to PDF file
- **Output**: Combined text from all pages
- **Technology**: PyPDF2 library
- **Error Handling**: Returns "[PDF Error]" on failure

##### `extract_text_from_docx(filepath)`

- **Input**: Path to DOCX/DOC file
- **Output**: Combined text from all paragraphs
- **Technology**: python-docx library

##### `extract_text_from_excel(filepath)`

- **Input**: Path to XLS/XLSX file
- **Output**: Combined cell content from all sheets
- **Technology**: openpyxl library

##### `extract_document_text(filepath)`

- **Input**: Any supported file path
- **Output**: Extracted text (auto-detects format)
- **Process**: Auto-routes to appropriate extractor

---

### 2. TextAnalyzer

NLP-based intelligent text analysis engine.

#### Methods

##### `detect_high_risk_keywords(text)`

**Purpose**: Identifies suspicious keywords in text

**Keywords Monitored** (20+):

```python
'cash', 'structured', 'smurfing', 'front', 'shell company',
'sanctions', 'embargo', 'terrorist', 'money laundering',
'hawala', 'underground banking', 'structuring', 'suspicious',
'investigation', 'fraud', 'offshore', 'tax evasion', 'bulk cash',
'trade based', 'customs', 'informal value transfer', 'black market'
```

**Returns**:

```python
(keyword_risk_score: int 0-100, found_keywords: list[str])
```

**Scoring**: +15 points per keyword found (capped at 100)

**Example**:

```python
risk, keywords = TextAnalyzer.detect_high_risk_keywords(
    "This shell company uses structuring for money laundering"
)
# Returns: (30, ['shell company', 'structuring', 'money laundering'])
```

---

##### `analyze_sentiment(text)`

**Purpose**: Determines emotional tone of document

**Technology**: TextBlob sentiment analysis

**Returns**:

```python
polarity: float  # Range: -1.0 (negative) to +1.0 (positive)
```

**Interpretation**:

- **-1.0 to -0.5**: Very negative/suspicious tone
- **-0.5 to 0**: Negative/cautious
- **0 to 0.5**: Positive/normal
- **0.5 to 1.0**: Very positive/confidence

**Example**:

```python
sentiment = TextAnalyzer.analyze_sentiment(
    "Urgent suspicious transaction flagged for investigation"
)
# Returns: -0.45 (negative sentiment)
```

---

##### `detect_entity_types(text)`

**Purpose**: Extracts named entities (NER)

**Technology**: NLTK Named Entity Chunker

**Returns**:

```python
entity_types: list[str]  # Unique entity type labels
```

**Entity Types Detected**:

- **PERSON**: Individual names
- **ORG**: Organization/Company names
- **GPE**: Countries/Cities/States
- **LOCATION**: Physical locations
- **DATE**: Dates and times
- **MONEY**: Currency amounts
- **PERCENT**: Percentages
- **FACILITY**: Buildings/Airports

**Example**:

```python
entities = TextAnalyzer.detect_entity_types(
    "John Smith at ABC Corporation transferred $50,000 to Pakistan"
)
# Returns: ['PERSON', 'ORG', 'MONEY', 'GPE']
```

---

##### `calculate_text_complexity(text)`

**Purpose**: Measures document sophistication

**Formula**:

```
Complexity = (word_count / 100) × 10 + (avg_word_length / 5) × 5
```

**Returns**:

```python
complexity_score: float  # Range: 0-100
```

**Interpretation**:

- **0-20**: Simple/basic language
- **20-40**: Standard/normal complexity
- **40-60**: Complex/technical content
- **60-80**: Very complex/sophisticated
- **80-100**: Highly complex/obfuscated

**Example**:

```python
complexity = TextAnalyzer.calculate_text_complexity(
    "This transaction exhibits characteristics of potential structuring..."
)
# Returns: 65.2 (highly complex)
```

---

### 3. AIAssessment

Main intelligence engine for comprehensive risk assessment.

#### Methods

##### `generate_risk_score(amount, velocity, country_risk, pep_match, document_risk=0)`

**Purpose**: Calculates comprehensive risk score

**Parameters**:

- `amount`: Transaction amount (float)
- `velocity`: Transaction frequency (0-1, normalized)
- `country_risk`: Geographic risk level (0-1)
- `pep_match`: PEP connection probability (0-1)
- `document_risk`: Document analysis risk (0-100, optional)

**Scoring Logic**:

```python
score = 0

if amount > 5,000,000:
    score += 30  # Large transaction
elif amount > 1,000,000:
    score += 20  # Medium-large transaction

score += velocity × 10       # Velocity multiplier
score += country_risk × 8    # Geographic risk
score += pep_match × 15      # PEP connection weight
score += (document_risk / 100) × 25  # Document intelligence weight

return min(100, score)  # Cap at 100
```

**Returns**:

```python
risk_score: int  # Range: 0-100
```

**Example**:

```python
score = AIAssessment.generate_risk_score(
    amount=2000000,
    velocity=0.8,
    country_risk=0.7,
    pep_match=0.5,
    document_risk=45
)
# Returns: 78 (HIGH RISK)
```

---

##### `analyze_factors(case_data, document_text="")`

**Purpose**: Analyzes all risk factors including document intelligence

**Parameters**:

- `case_data`: Dictionary with case information
- `document_text`: Combined extracted text from documents (optional)

**Returns**:

```python
{
    "velocity": 7,                    # Transaction velocity
    "geographic_risk": 6,             # Country risk
    "sanctions_match": 4,             # Sanctions list match
    "structuring": 5,                 # Structuring pattern
    "pep_connection": 3,              # PEP match
    "document_risk": 2.5,             # NEW: Document analysis
    "keywords_detected": [...],       # Found high-risk keywords
    "sentiment": -0.15,               # Document sentiment
    "complexity": 42.5,               # Document complexity
    "entities": ["PERSON", "ORG"]     # Named entities
}
```

---

##### `get_recommendations(risk_score, document_findings=None)`

**Purpose**: Generates context-aware recommendations

**Risk Score Thresholds**:

- **≥80**: LEA Referral, Block, Escalate, Investigation
- **≥60**: EDD, Further verification, Document, Contact
- **<60**: KYC sufficient, Monitor, File, Proceed

**Document-based Additions**:

- If keywords found: "⚠️ Suspicious keywords: [list]"
- If entities detected: "📋 Entities: [list]"

**Returns**:

```python
recommendations: list[str]  # Action items with emojis
```

**Example Response**:

```python
[
    "📋 Enhanced Due Diligence",
    "🔎 Further verification",
    "💾 Document everything",
    "📞 Contact customer",
    "⚠️ Suspicious keywords found: shell company, offshore",
    "📋 Entities detected: PERSON, ORG, GPE"
]
```

---

##### `intelligent_assess(case_id, case_data, uploaded_files=None)`

**Purpose**: Comprehensive one-call assessment with all intelligence

**Parameters**:

- `case_id`: Unique case identifier
- `case_data`: Case information dictionary
- `uploaded_files`: List of file paths to analyze

**Process**:

1. Extract text from all uploaded files
2. Run comprehensive analysis on combined text
3. Detect keywords and calculate keyword risk
4. Analyze sentiment and entities
5. Calculate document risk score
6. Generate complete factors analysis
7. Calculate final risk score
8. Generate recommendations
9. Return complete assessment object

**Returns**:

```python
{
    'risk_score': 72,
    'risk_level': '🔴 CRITICAL',
    'factors': {...},
    'recommendations': [...],
    'document_findings': {
        'keyword_risk': 45,
        'high_risk_keywords': ['shell company', 'structuring'],
        'entities': ['PERSON', 'ORG', 'GPE'],
        'sentiment': -0.32,
        'complexity': 58.3,
        'text_length': 8234
    }
}
```

**Example**:

```python
assessment = AIAssessment.intelligent_assess(
    case_id="case-123",
    case_data={'amount': 5000000, 'title': 'Suspicious Transfer'},
    uploaded_files=['uploads/kyc.pdf', 'uploads/bank_stmt.xlsx']
)
```

---

## Integration Examples

### Example 1: Simple File Analysis

```python
# Extract and analyze a single document
filepath = "uploads/kyc_document.pdf"
text = DocumentProcessor.extract_document_text(filepath)

# Analyze the text
keyword_risk, keywords = TextAnalyzer.detect_high_risk_keywords(text)
sentiment = TextAnalyzer.analyze_sentiment(text)
entities = TextAnalyzer.detect_entity_types(text)

print(f"Keywords found: {keywords}")
print(f"Sentiment: {sentiment}")
print(f"Entities: {entities}")
```

### Example 2: Complete Case Assessment

```python
# Full assessment with documents
case_data = {
    'amount': 2500000,
    'title': 'Suspicious Transfer',
    'category': 'Wire Transfer'
}

files = [
    'uploads/kyc.pdf',
    'uploads/bank_statement.xlsx',
    'uploads/id_photo.jpg'
]

assessment = AIAssessment.intelligent_assess(
    case_id='case-456',
    case_data=case_data,
    uploaded_files=files
)

print(f"Risk Score: {assessment['risk_score']}")
print(f"Risk Level: {assessment['risk_level']}")
print(f"Files Analyzed: {len(files)}")
```

### Example 3: Custom Keyword Detection

```python
# Add custom high-risk keywords to detection
custom_text = "Transaction involves multiple beneficiaries in jurisdictions with high ML/TF risk"

risk_score, keywords = TextAnalyzer.detect_high_risk_keywords(custom_text)
print(f"Detected risk level: {risk_score}/100")

if risk_score >= 60:
    print("⚠️ ALERT: High-risk keywords detected!")
```

---

## Performance Considerations

### File Size Limits

- **Images**: Up to 500MB (OCR slower for large files)
- **PDFs**: Up to 500MB (multipage processing time increases)
- **Excel**: Up to 500MB (sheet extraction varies by size)
- **Total Upload**: 500MB max per file

### Processing Time Estimates

- **Small PDF (< 5 pages)**: 0.5-1 second
- **Large PDF (50+ pages)**: 5-10 seconds
- **OCR Image**: 2-5 seconds per image
- **Excel Sheet**: 1-3 seconds per sheet
- **Full Assessment (3 files)**: 5-15 seconds

### Optimization Tips

1. Upload one document type at a time for faster processing
2. Use PDF instead of images when possible (faster OCR-free)
3. Compress large images before uploading
4. Run assessments after document batch upload

---

## Error Handling

### Common Errors & Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "[Image - no readable text]" | OCR failed or image unclear | Upload clearer scan/photo |
| "FileNotFoundError" | File deleted after upload | Re-upload document |
| "UnicodeDecodeError" | Text encoding issue | Verify file format |
| "Timeout" | Processing taking too long | Split into smaller files |

---

## Future Enhancements

- [ ] Machine Learning sentiment analysis
- [ ] Custom keyword rule engine
- [ ] Real-time OFAC list matching
- [ ] Multi-language support
- [ ] Audio transcription capability
- [ ] Video content analysis
- [ ] Blockchain transaction tracing

---

**Last Updated**: February 1, 2026
**API Version**: 2.0
**System**: Advanced AML v9.0
