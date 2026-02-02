# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies (One-time)

**Option A: Using Setup Script (Recommended)**

```bash
python setup.py
```

**Option B: Manual Installation**

```bash
pip install -r requirements.txt
```

---

### Step 2: Start the Backend Server

**Option A: Windows Users**

```bash
double-click START_SERVER.bat
```

**Option B: Command Line**

```bash
python aml_system.py
```

**Expected Output:**

```
INFO - AML AML Case Management System v3.0 started
INFO - Database initialized successfully
INFO - Flask application initialized successfully
INFO - Server running on http://0.0.0.0:5000
```

---

### Step 3: Open the Frontend

1. Right-click on `aml3_system.html`
2. Select "Open with" > "Your Browser"
3. Or copy the file path and paste in address bar

**Or directly:** Double-click `aml3_system.html`

---

### Step 4: Verify Installation

**Run the test suite:**

```bash
python test_api.py
```

Expected output: All tests should show PASS ✓

---

## ✨ Key Features to Try

### 1. Create a New Case

1. Scroll to "New Case Entry" section
2. Fill in the form:
   - Enquiry Number: `TEST/2024`
   - Date: Today's date
   - Source: FMU
   - Category: STR
   - Accused Names: Sample Subject A
   - CNIC: 00000-0000000-0
   - Allegation: Test hawala operations
   - Amount: 2500000
3. Press **Ctrl+S** or click "Save Case"

### 2. View Dashboard

- Dashboard auto-loads on startup
- Shows real-time statistics
- Updates every 5 minutes

### 3. Export Cases

1. Click "Export Cases" (if button available)
2. Or press **Ctrl+E**
3. CSV file downloads automatically

### 4. GitHub Integration

- Automatically syncs data from GitHub
- View repository info
- Fetch external case data

---

## 🔍 Monitoring

### Check Server Status

```bash
curl http://localhost:5000/api/health
```

### View Logs

```bash
type aml_system.log
```

### Test an API Endpoint

```bash
curl http://localhost:5000/api/cases?limit=5
```

---

## 🛠️ Configuration

Edit `.env` file to customize:

```env
FLASK_ENV=production          # production or development
API_PORT=5000                 # Change port if needed
GITHUB_REPO_OWNER=AML-AMLC   # GitHub owner
GITHUB_REPO_NAME=aml-case-data  # GitHub repo
```

---

## ⚠️ Troubleshooting

### "Port 5000 already in use"

```bash
# Stop other instances or use different port
# Edit .env: API_PORT=5001
```

### "No module named 'flask'"

```bash
pip install -r requirements.txt
```

### "Database locked"

```bash
# Delete database and restart
del aml_system.db
python aml_system.py
```

### Frontend not connecting to API

- Make sure backend is running: `python aml_system.py`
- Check browser console for errors: Press F12
- Verify API is accessible: `http://localhost:5000/api/health`

---

## 📊 Default Test Data

The system comes with:

- Empty database (auto-initialized)
- Pre-configured tables
- Ready to accept data

### Add Test Data

1. Use the web form to create cases
2. Or use the API directly:

```bash
curl -X POST http://localhost:5000/api/cases \
  -H "Content-Type: application/json" \
  -d '{
    "enquiry_number": "001/2024",
    "date_created": "2024-01-31",
    "source": "FMU",
    "category": "STR",
    "accused_names": ["Test Person"],
    "cnic_numbers": ["00000-0000000-0"],
    "allegation_summary": "Test case",
    "amount_pkr": 1000000,
    "sensitivity_level": "normal"
  }'
```

---

## 📚 Learn More

| File | Purpose |
|------|---------|
| README.md | Full documentation |
| API_DOCUMENTATION.md | API reference |
| aml_system.py | Backend source code |
| aml3_system.html | Frontend code |

---

## 🆘 Need Help?

1. **Check logs:** `aml_system.log`
2. **Run tests:** `python test_api.py`
3. **Read docs:** `README.md`
4. **Contact:** AML AMLC Lahore

---

## ✅ You're All Set

- ✓ Backend: Running on localhost:5000
- ✓ Frontend: Open in browser
- ✓ Database: SQLite initialized
- ✓ API: Ready to use
- ✓ Logging: Active
- ✓ GitHub: Integrated

**Happy investigating!** 🕵️

---

*AML AML Case Management System v3.0*  
*Developed by: Waqas Khan Niazi, AML AMLC Lahore*

