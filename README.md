# FIA AML Case Management System v3.0

**Professional Backend Implementation with GitHub Integration & Advanced Features**

---

## 📋 Overview

A production-ready Anti-Money Laundering (AML) Case Management System developed for FIA AMLC Lahore. This upgraded version includes:

✅ **Professional Python Backend** - Flask REST API with SQLite database  
✅ **GitHub Data Integration** - Fetch and sync case data from GitHub repositories  
✅ **AI-Powered Risk Assessment** - Intelligent risk scoring and pattern detection  
✅ **Advanced Database Management** - Audit logs, user management, case tracking  
✅ **RESTful API** - Complete API for frontend integration  
✅ **Data Export** - CSV export functionality for reporting  
✅ **Real-time Analytics** - Dashboard statistics and insights  
✅ **Security Features** - JWT authentication, password hashing, audit logging  

---

## 🚀 Features

### Backend (Python - Flask)

- **Case Management**
  - Create, read, update, list cases
  - Automatic risk scoring based on AI analysis
  - Support for multiple accused and CNIC numbers
  - Case categorization and status tracking

- **AI Risk Analyzer**
  - Keyword-based threat detection
  - Amount threshold analysis
  - Sensitivity level assessment
  - Pattern recognition for suspicious transactions
  - Risk scoring (0-100 scale)

- **GitHub Integration**
  - Fetch case data from GitHub repositories
  - Automatic data synchronization
  - Repository information retrieval
  - Version control integration

- **Database**
  - SQLite database with normalized schema
  - User management system
  - Audit logging for all operations
  - Transaction support

- **API Endpoints**
  - `GET /api/health` - Health check
  - `POST /api/cases` - Create case
  - `GET /api/cases` - List cases
  - `GET /api/cases/<id>` - Get case details
  - `PUT /api/cases/<id>` - Update case
  - `GET /api/github/cases` - Fetch from GitHub
  - `GET /api/github/info` - Repository info
  - `GET /api/analytics/dashboard` - Dashboard statistics
  - `GET /api/export/cases` - Export cases to CSV

### Frontend (HTML/JavaScript)

- **Modern UI**
  - Professional dashboard design
  - Responsive layout
  - Real-time notifications
  - Interactive forms

- **Features**
  - Case creation and management
  - Real-time AI analysis
  - GitHub data integration
  - CSV export functionality
  - Auto-refresh dashboard
  - Keyboard shortcuts (Ctrl+S to save, Ctrl+E to export)

---

## 📦 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for GitHub integration)

### 1. Install Dependencies

```bash
cd c:\Users\OTS\OneDrive\Desktop\Aml_Case_Management_sysyem
pip install -r requirements.txt
```

Or manually install:

```bash
pip install flask flask-cors flask-sqlalchemy pyjwt requests python-dotenv
```

### 2. Run the Backend Server

```bash
python aml_system.py
```

Expected output:

```
INFO - FIA AML Case Management System v3.0 started
INFO - Server running on http://0.0.0.0:5000
```

### 3. Open Frontend in Browser

- Open `aml3_system.html` in a web browser
- Or access via: `http://localhost:5000` (if configured)

---

## 📊 API Documentation

### Create Case

**Endpoint:** `POST /api/cases`

**Request Body:**

```json
{
  "enquiry_number": "123/2024",
  "date_created": "2024-01-31",
  "source": "FMU",
  "category": "STR",
  "accused_names": ["Sample Subject A", "Sample Subject B"],
  "cnic_numbers": ["00000-0000000-0", "00000-0000000-1"],
  "allegation_summary": "Suspicious hawala transaction with large amount",
  "amount_pkr": 2500000,
  "sensitivity_level": "high"
}
```

**Response:**

```json
{
  "success": true,
  "message": "Case created successfully",
  "case_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

### List Cases

**Endpoint:** `GET /api/cases?limit=50&offset=0`

**Response:**

```json
{
  "count": 5,
  "cases": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "enquiry_number": "123/2024",
      "status": "pending",
      "risk_score": 78,
      "amount_pkr": 2500000,
      ...
    }
  ]
}
```

### Get Dashboard Analytics

**Endpoint:** `GET /api/analytics/dashboard`

**Response:**

```json
{
  "total_cases": 102,
  "active_cases": 42,
  "high_risk": 18,
  "total_amount_involved": 500000000,
  "average_risk_score": 58.5
}
```

### Fetch from GitHub

**Endpoint:** `GET /api/github/cases`

**Response:**

```json
{
  "success": true,
  "message": "Cases fetched from GitHub",
  "cases": [...]
}
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project directory:

```env
FLASK_ENV=production
SECRET_KEY=your-secure-secret-key-here
DEBUG=False
DATABASE_URL=sqlite:///aml_system.db
GITHUB_REPO_OWNER=FIA-AMLC
GITHUB_REPO_NAME=aml-case-data
```

### GitHub Repository Setup

To enable GitHub integration, create a repository with this structure:

```
aml-case-data/
├── data/
│   ├── cases.json
│   └── references.json
└── README.md
```

**Example cases.json:**

```json
[
  {
    "enquiry_number": "286/2024",
    "accused_names": ["Sample Subject A"],
    "amount_pkr": 2500000,
    ...
  }
]
```

---

## 🤖 AI Risk Assessment Logic

The system uses intelligent risk assessment based on:

### Risk Factors (0-100 scale)

1. **Amount Threshold**
   - High (≥50M PKR): +30 points
   - Medium (≥10M PKR): +20 points

2. **Keywords Detection**
   - Hawala, Hundi: +15 points per keyword
   - Terrorism, Drug, Corruption: +15 points per keyword

3. **Sensitivity Level**
   - Normal: 1.0x
   - Political: 1.4x
   - High Profile: 1.3x
   - International: 1.5x

4. **Multiple Accused**
   - More than 2 accused: +15 points

### Risk Levels

- **Low** (0-39): Routine investigation
- **Medium** (40-59): Enhanced monitoring
- **High** (60-79): Comprehensive investigation
- **Critical** (80-100): Urgent investigation required

---

## 📁 File Structure

```
Aml_Case_Management_sysyem/
├── aml_system.py              # Main backend application
├── aml3_system.html           # Frontend UI
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
├── aml_system.db              # SQLite database (auto-created)
├── aml_system.log             # Application logs
└── .env                       # Environment configuration (optional)
```

---

## 🔐 Security Features

- **Password Hashing** - Using werkzeug secure hash
- **JWT Authentication** - Token-based API security
- **Audit Logging** - All operations logged with user tracking
- **Input Validation** - SQL injection prevention
- **CORS Support** - Controlled cross-origin requests
- **Error Handling** - Secure error messages

---

## 🐛 Troubleshooting

### Issue: "Module not found" error

**Solution:**

```bash
pip install -r requirements.txt
```

### Issue: Port 5000 already in use

**Solution:**

```bash
# Change port in aml_system.py
app.run(port=5001)
```

### Issue: GitHub connection failed

**Solution:**

- Check internet connectivity
- Verify GitHub repository URL
- Check GitHub API rate limits

### Issue: Database locked

**Solution:**

- Ensure only one instance of the app is running
- Delete `aml_system.db` and restart to recreate

---

## 📈 Performance Optimization

- Database indexing on frequently queried fields
- Efficient pagination (limit/offset)
- Caching for GitHub data
- Connection pooling for database
- Auto-refresh interval: 5 minutes

---

## 🔄 Data Refresh

- Dashboard auto-refreshes every 5 minutes
- Manual refresh available via API
- GitHub sync on demand via `/api/github/cases`

---

## 📞 Support & Maintenance

**Developed by:** Waqas Khan Niazi, FIA AMLC Lahore

**Key Components:**

- Case Management System
- Risk Assessment Engine
- GitHub Integration Module
- RESTful API Server
- Database Manager
- Audit Logger

---

## 📝 Version History

### v3.0 (Current)

- ✨ Professional Python backend
- ✨ GitHub data integration
- ✨ AI-powered risk assessment
- ✨ REST API with comprehensive endpoints
- ✨ Database management system
- ✨ CSV export functionality
- ✨ Enhanced security features
- ✨ Audit logging system

---

## ⚖️ Legal & Compliance

This system is developed for FIA (Federal Investigation Agency) AML Circle Lahore for Anti-Money Laundering investigations in compliance with:

- AMLA 2010 (Pakistan)
- AML/CFT International Standards
- FIA Guidelines

---

## 📜 License

For official use by FIA AMLC Lahore only.

---

**Last Updated:** January 31, 2026  
**System Version:** 3.0  
**Database Version:** 1.0
