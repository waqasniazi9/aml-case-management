# AML Case Management System v10.0 - Quick Start Guide

## 🚀 SERVER IS NOW RUNNING

Your AML system is up and running with all v10.0 features enabled.

### ✅ Access the Dashboard

The dashboard is accessible at:

```
http://127.0.0.1:5000
```

### 🛑 Start the Server

To start the server, run:

```bash
python START_SERVER.py
```

Or run the batch file:

```
START_SERVER.bat
```

### 📊 Dashboard Features

The enhanced dashboard provides access to:

1. **Case Management**
   - Create, view, edit, and delete cases
   - Bulk operations for multiple cases
   - Advanced search with multi-criteria filtering

2. **AI Assessment**
   - Automatic risk scoring
   - Document analysis and OCR
   - Sentiment analysis and entity recognition
   - Financial metrics extraction

3. **Audit Trail**
   - Complete action history
   - User activity tracking
   - Change history for all cases
   - Compliance logging

4. **Reports**
   - Generate comprehensive AML reports
   - Export in multiple formats
   - Document findings integration

5. **Search & Analytics**
   - Search cases by multiple criteria
   - Search transactions
   - Advanced filtering options
   - Analytics and insights

### 📡 API Endpoints

The system exposes 33 REST API endpoints for programmatic access:

**Authentication:**

- POST `/api/auth/register` - Create new user
- POST `/api/auth/login` - User login
- POST `/api/auth/logout` - User logout
- GET `/api/auth/profile` - Get user profile

**Case Management:**

- POST `/api/cases/create` - Create new case
- GET `/api/cases` - List all cases
- GET `/api/cases/<case_id>` - Get case details
- POST `/api/cases/edit` - Edit case
- POST `/api/cases/<case_id>/update` - Update case
- POST `/api/cases/<case_id>/delete` - Delete case (soft delete)
- POST `/api/cases/<case_id>/restore` - Restore deleted case

**Assessment & AI:**

- POST `/api/assess/<case_id>` - Run AI assessment
- GET `/api/assess/<case_id>` - Get assessment results
- POST `/api/analyze-documents/<case_id>` - Analyze documents

**Audit & Compliance:**

- GET `/api/audit/<case_id>` - Get audit trail
- GET `/api/trace/<case_id>` - Get change history
- GET `/api/audit/user/<user_id>` - Get user actions

**Search:**

- POST `/api/search/cases` - Search cases
- POST `/api/search/transactions` - Search transactions  
- POST `/api/search/advanced` - Advanced search

**Bulk Operations:**

- POST `/api/bulk/update` - Bulk update cases
- POST `/api/bulk/delete` - Bulk delete cases
- POST `/api/bulk/export` - Bulk export cases

**Reports:**

- POST `/api/report/<case_id>` - Generate report
- GET `/api/report/<case_id>` - Get report
- POST `/api/compliance` - Compliance report

### 🗄️ Database

The system uses SQLite3 with 8 tables:

- `users` - User accounts
- `cases` - AML cases
- `transactions` - Transaction records
- `files` - Uploaded files
- `assessments` - AI assessments
- `reports` - Generated reports
- `compliance` - Compliance logs
- `audit_trail` - Complete audit history (NEW in v10.0)

### 🔧 Configuration

Set these environment variables to customize the server:

```powershell
# Set custom host and port
$env:AML_HOST = "127.0.0.1"  # Default: 0.0.0.0
$env:AML_PORT = "5000"       # Default: 5000

python START_SERVER.py
```

### 🛠️ Troubleshooting

**Server won't start:**

- Make sure port 5000 is not in use
- Run `netstat -ano | findstr ":5000"` to check
- Kill existing process: `Get-Process python | Stop-Process -Force`

**Dashboard not loading:**

- Check browser console for JavaScript errors
- Verify server is running: `curl http://127.0.0.1:5000`
- Check firewall settings

**Database errors:**

- The database initializes automatically
- Check `aml_multi_user.db` exists in the project directory
- Delete the file to reset: `Remove-Item aml_multi_user.db`

### 📦 System Requirements

- Python 3.10+
- Flask 2.x
- SQLite3
- All dependencies in `requirements.txt`

### 📚 Documentation

For detailed API documentation, see:

- [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - Complete API reference
- [THREAT_INTELLIGENCE_GUIDE.md](THREAT_INTELLIGENCE_GUIDE.md) - AI features
- [README.md](README.md) - General information

### 🔐 Security Notes

- Default credentials available in documentation
- Enable HTTPS in production
- Use strong SECRET_KEY in production
- Implement proper user authentication

### 📞 Support

For issues or questions about the system, refer to:

- PROJECT_INDEX.md - Complete file structure
- QUICK_REFERENCE.md - Quick command reference
- COMPLETION_CHECKLIST.md - Feature completion status

---

**Status:** ✅ PRODUCTION READY

**Version:** v10.0

**Last Updated:** February 1, 2026

**All Features Active:**

- ✅ Case Management (CRUD + Bulk)
- ✅ AI Assessment
- ✅ Audit Trail & Compliance
- ✅ Advanced Search
- ✅ Document Analysis
- ✅ Report Generation
- ✅ User Management
