# 🤖 Enhanced AI Assessment System - Complete Guide

## Overview

The AML Case Management System now features an **Intelligent Document Processing Engine** with advanced NLP (Natural Language Processing) capabilities that automatically analyze documents, extract insights, and enhance risk scoring.

---

## 🎯 Key Features

### 1. **Intelligent Document Processing**

- **OCR (Optical Character Recognition)**: Extract text from images (JPG, PNG, GIF)
- **PDF Parsing**: Read and analyze PDF documents
- **Word Documents**: Extract content from .DOC and .DOCX files
- **Excel Sheets**: Process .XLS and .XLSX spreadsheets
- **Text Files**: Direct text analysis from TXT files
- **Auto-Detection**: System automatically detects file type and processes accordingly

### 2. **Advanced Text Analysis**

- **Keyword Detection**: Identifies 20+ high-risk keywords indicating suspicious activity
  - Money laundering, structuring, sanctions, shell companies, terrorist financing, etc.
- **Sentiment Analysis**: Analyzes emotional tone of document content
- **Entity Recognition**: Extracts people, organizations, and locations using NLP
- **Text Complexity Scoring**: Measures document sophistication level
- **Named Entity Extraction**: Identifies specific entities in documents

### 3. **Enhanced Risk Scoring**

Traditional factors PLUS document intelligence:

- Transaction Velocity (7/10)
- Geographic Risk (6/10)
- Sanctions Match (4/10)
- Structuring Pattern (5/10)
- PEP Connection (3/10)
- **NEW: Document Risk** (analyzed from uploaded files)

Final risk score combines all factors: **0-100 scale**

### 4. **Intelligent Recommendations**

System generates context-aware recommendations based on:

- Risk score threshold
- High-risk keywords found
- Entity types detected
- Document complexity analysis

---

## 📊 How It Works

### Step 1: Upload Documents

Users can upload multiple file types for a case:

- KYC documents (identity verification)
- CDD (Customer Due Diligence) records
- EDD (Enhanced Due Diligence) files
- Financial statements and invoices
- Photos and video evidence
- Any supporting documentation

### Step 2: Automatic Text Extraction

System extracts text from each document:

```
Image → OCR → Text
PDF → Parser → Text
Word → Reader → Text
Excel → Sheets Reader → Text
```

### Step 3: Intelligent Analysis

For each document:

1. Extract text content
2. Scan for high-risk keywords (15 points per match)
3. Analyze sentiment (-1 to +1 scale)
4. Extract named entities (NER)
5. Calculate text complexity

### Step 4: Risk Calculation

```
Document Risk = (Keyword Risk / 5) + |Sentiment × 20| + (Complexity / 10)
Overall Risk = Base Score + (Document Risk × 0.25)
```

### Step 5: Generate Report

Comprehensive report includes:

- Case information
- All factors analysis
- **Document Intelligence section**
- High-risk keywords found
- Entity types detected
- Recommendations

---

## 🔍 High-Risk Keywords Detected

The system monitors for:

- **Financing**: cash, bulk cash, informal value transfer, hawala, underground banking
- **Smuggling**: trade based, structuring, smurfing, smuggling
- **Legal Issues**: sanctions, embargo, terrorist, money laundering, fraud, tax evasion
- **Suspicious Entities**: front, shell company, offshore, investigation

**Risk Score**: +15 points per keyword found (max 100)

---

## 📱 API Endpoints

### 1. **Run Assessment with Document Analysis**

```
POST /api/assess/<case_id>
```

**Response**:

```json
{
  "assessment_id": "uuid",
  "risk_score": 65,
  "risk_level": "🟠 HIGH",
  "factors": {
    "velocity": 7,
    "geographic_risk": 6,
    "sanctions_match": 4,
    "structuring": 5,
    "pep_connection": 3,
    "document_risk": 2.5,
    "keywords_detected": ["shell company", "structuring"],
    "sentiment": -0.15,
    "complexity": 42.5,
    "entities": ["PERSON", "ORG", "GPE"]
  },
  "recommendations": [
    "📋 Enhanced Due Diligence",
    "🔎 Further verification",
    "⚠️ Suspicious keywords found: shell company, structuring",
    "📋 Entities detected: PERSON, ORG"
  ],
  "document_findings": {
    "keyword_risk": 30,
    "high_risk_keywords": ["shell company", "structuring"],
    "entities": ["PERSON", "ORG", "GPE"],
    "sentiment": -0.15,
    "complexity": 42.5,
    "text_length": 5432
  },
  "files_analyzed": 3
}
```

### 2. **Analyze Uploaded Documents**

```
POST /api/assess/<case_id>/documents
```

**Response**:

```json
{
  "case_id": "case-123",
  "documents_analyzed": 2,
  "analysis": [
    {
      "filename": "kyc_document.pdf",
      "text_length": 2541,
      "keyword_risk": 15,
      "keywords_found": ["shell company"],
      "sentiment": -0.25,
      "entities": ["PERSON", "ORG"],
      "text_preview": "This entity is a shell company registered offshore..."
    },
    {
      "filename": "bank_statement.xlsx",
      "text_length": 1245,
      "keyword_risk": 30,
      "keywords_found": ["cash", "structured"],
      "sentiment": -0.10,
      "entities": ["ORG"],
      "text_preview": "Transaction pattern shows structured deposits..."
    }
  ]
}
```

---

## 💡 Usage Examples

### Example 1: Simple Case Assessment

1. Create a case with basic info
2. Click "AI Assessment" tab
3. System auto-analyzes any uploaded documents
4. Get instant risk score and recommendations

### Example 2: Document-Heavy Investigation

1. Upload KYC, CDD, EDD documents
2. Upload bank statements (Excel/PDF)
3. Upload photos (ID, documents)
4. Run assessment
5. System extracts text from all files
6. Analyzes combined content for:
   - Suspicious keywords
   - Entity patterns
   - Complexity indicators
7. Generates comprehensive report

### Example 3: Report Generation

1. After assessment, go to "Reports" tab
2. Select "Generate Report"
3. System creates report including:
   - All document intelligence findings
   - High-risk keywords discovered
   - Entity types detected
   - Combined sentiment analysis
4. Download as TXT/PDF/Excel

---

## 📈 Risk Score Interpretation

| Score | Level | Status | Action |
|-------|-------|--------|--------|
| 0-20  | 🟢 LOW | Clear | Proceed normally |
| 21-40 | 🟡 MEDIUM | Monitor | Standard monitoring |
| 41-60 | 🟠 HIGH | Alert | Enhanced due diligence |
| 61-80 | 🔴 CRITICAL | Block | Investigation required |
| 81-100 | 🔴 CRITICAL | Urgent | LEA referral recommended |

---

## 🛡️ Supported File Types

| Category | Formats | Processing |
|----------|---------|-----------|
| Images | JPG, PNG, GIF, BMP, TIFF | OCR + text extraction |
| Documents | PDF, DOCX, DOC | Text parsing |
| Spreadsheets | XLSX, XLS | Cell content extraction |
| Text | TXT | Direct reading |
| Video | MP4, MOV | Metadata only |

---

## 🚀 Advanced Features

### 1. **Entity Recognition**

Identifies:

- **PERSON**: Individual names
- **ORG**: Organization/Company names
- **GPE**: Geographic/Political entities
- **LOCATION**: Physical locations

### 2. **Sentiment Analysis**

- **Positive** (+1 to 0): Normal business language
- **Negative** (-1 to 0): Suspicious tone, evasive language
- **Neutral** (~0): Factual documentation

### 3. **Document Complexity**

Measures sophistication based on:

- Word count
- Sentence structure
- Average word length
- Technical terminology

---

## 🔧 System Architecture

```
Document Upload
       ↓
Auto-Detection (file type)
       ↓
Text Extraction (OCR/Parser)
       ↓
NLP Analysis (keywords, entities, sentiment)
       ↓
Risk Calculation
       ↓
Recommendation Generation
       ↓
Report Creation
```

---

## ⚙️ Configuration

### High-Risk Keywords List

Edit in `TextAnalyzer.detect_high_risk_keywords()`:

```python
high_risk = [
    'cash', 'structured', 'smurfing', 'shell company',
    'sanctions', 'money laundering', ...
]
```

### Risk Weighting

Modify in `AIAssessment.generate_risk_score()`:

```python
score += (document_risk / 100) * 25  # Adjust multiplier (25)
```

### NLTK Data Download

System automatically downloads:

- Punkt tokenizer
- POS tagger
- WordNet lemmatizer

---

## 📊 Sample Report

```
AML RISK ASSESSMENT & COMPLIANCE REPORT v9.0
Enhanced AI Document Intelligence System

CASE INFORMATION:
Case ID: case-456
Title: Suspicious Currency Exchange
Amount: PKR 50,000,000
Status: Open

AI RISK ASSESSMENT:
Overall Risk Score: 72/100
Risk Level: 🔴 CRITICAL

DOCUMENT ANALYSIS & INTELLIGENCE:
Total Text Processed: 8,234 characters
Keyword Risk Score: 45/100
Sentiment Analysis: -0.32
Text Complexity: 58.3
High-Risk Keywords Found: shell company, structured, offshore
Entities Detected: PERSON, ORG, GPE

FACTOR ANALYSIS:
Transaction Velocity: 7/10
Geographic Risk: 6/10
Document Risk: 4.5/10

AI RECOMMENDATIONS:
1. ⚠️ LEA Referral recommended
2. ❌ Block account immediately
3. ⚠️ Suspicious keywords found: shell company, structured, offshore
4. 📋 Entities detected: PERSON, ORG, GPE
```

---

## 🎓 Best Practices

1. **Upload Multiple Documents**: More files = better analysis
2. **Clear Documentation**: Use legible scans/photos for OCR
3. **Regular Assessment**: Run assessment after each document upload
4. **Review Recommendations**: Don't ignore AI suggestions
5. **Document Everything**: Keep all analysis reports

---

## 🔐 Security & Privacy

- All text analysis happens locally (no cloud upload)
- Documents stored in `/uploads` folder
- Database encrypted at rest
- User data isolated per multi-user account
- No sensitive text exported in logs

---

## 📞 Support

For issues:

1. Check document file format and size
2. Verify all required fields are filled
3. Ensure documents are readable
4. Check system logs for specific errors
5. Run fresh assessment if needed

---

**Last Updated**: February 1, 2026
**System Version**: v9.0 - Enhanced AI Assessment
**Developer**: Waqas Khan Niazi
