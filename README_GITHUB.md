# 🏦 Advanced AML Case Management System v9.0

A professional, multi-user Anti-Money Laundering (AML) compliance platform with AI-powered risk assessment, real-time transaction monitoring, and comprehensive compliance reporting.

## 🌟 Features

### Core Functionality

- **KYC & CDD Verification** - Know Your Customer and Customer Due Diligence workflows
- **Case Management** - Create, track, and manage AML cases with full CRUD operations
- **Real-Time Transaction Monitoring** - Monitor suspicious transaction patterns
- **AI Risk Assessment** - Automatic risk scoring using machine learning algorithms
- **Compliance Reporting** - Generate comprehensive compliance reports
- **Sanctions Screening** - Screen against OFAC, UN, EU, UK, Pakistan FIA, and Interpol lists
- **PEP Detection** - Politically Exposed Person verification
- **File Management** - Upload and manage KYC, CDD, EDD documents and media

### Technical Features

- 🔐 **Multi-User Authentication** - Secure login with password hashing (PBKDF2)
- 🌐 **Public URL Access** - Deploy online using ngrok with automatic tunnel
- 📱 **Responsive Dashboard** - Works on desktop and mobile devices
- 🔄 **Dynamic API Routing** - Automatically detects localhost vs remote access
- 📊 **Real-Time Search** - Search cases and transactions instantly
- 💾 **SQLite Database** - Lightweight, file-based database

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- ngrok account (for public deployment) - <https://dashboard.ngrok.com>

### Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/aml-case-management.git
cd aml-case-management

# Install dependencies
pip install -r requirements.txt

# Run the server
python start_server.py
```

Visit: **<http://127.0.0.1:5000>**

### Default Login

- **Username:** admin
- **Password:** admin123

## 🌍 Deploy Online

### Using ngrok (Recommended for Quick Testing)

```bash
# 1. Get ngrok from https://dashboard.ngrok.com
# 2. Add your authtoken
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE

# 3. Start Flask server (Terminal 1)
python start_server.py

# 4. Start ngrok tunnel (Terminal 2)
ngrok http 5000
```

Your public URL will appear in ngrok terminal:

```
Session URL: https://xxxx-yyyy-zzzz.ngrok-free.dev
```

### Using Production Cloud Platforms

See `DEPLOYMENT_GUIDE.md` for:

- PythonAnywhere
- Heroku
- AWS
- Azure
- DigitalOcean

## 📁 Project Structure

```
aml-case-management/
├── aml_system.py              # Main Flask application (1,915 lines)
├── start_server.py            # Server launcher script
├── dashboard_enhanced.html    # Frontend dashboard UI (1,280 lines)
├── aml_multi_user.db         # SQLite database
├── requirements.txt           # Python dependencies
├── config.py                  # Production configuration
├── wsgi.py                    # WSGI entry point for cloud deployment
├── API_DOCUMENTATION.md       # Complete API reference
├── DEPLOYMENT_GUIDE.md        # Cloud deployment instructions
├── README.md                  # This file
└── docs/                      # Additional documentation
```

## 🔌 API Endpoints (47 Total)

### Authentication

- `POST /api/auth/login` - User login
- `POST /api/auth/register` - New user registration
- `POST /api/auth/logout` - User logout

### Case Management

- `GET /api/cases` - Get all cases
- `POST /api/cases` - Create new case
- `GET /api/cases/<case_id>` - Get case details
- `PUT /api/cases/<case_id>` - Update case
- `DELETE /api/cases/<case_id>` - Delete case
- `GET /api/cases/search/<query>` - Search cases

### Transactions

- `GET /api/transactions` - Get all transactions
- `POST /api/transactions` - Add transaction
- `GET /api/transactions/<txn_id>` - Get transaction details
- `DELETE /api/transactions/<txn_id>` - Delete transaction

### AI Assessment

- `POST /api/assessment/analyze` - Generate AI risk assessment
- `GET /api/assessment/<case_id>` - Get assessment results

### Reports

- `POST /api/reports/generate` - Generate compliance report
- `GET /api/reports/<report_id>` - Get report

### File Management

- `POST /api/files/upload` - Upload documents
- `GET /api/files/list` - List uploaded files
- `DELETE /api/files/<file_id>` - Delete file

**See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for complete endpoint details.**

## 🛡️ Security Features

- ✅ PBKDF2 password hashing with SHA-256
- ✅ CORS enabled for cross-origin requests
- ✅ User authentication required for all endpoints
- ✅ Input validation on all forms
- ✅ SQL injection protection via parameterized queries
- ✅ Session management with user context

## 📊 Database Schema

### Tables

1. **users** - User accounts and authentication
2. **cases** - AML cases with risk assessment
3. **transactions** - Transaction records linked to cases
4. **ai_assessments** - AI-generated risk assessments
5. **compliance_checklist** - Compliance status tracking
6. **files** - Uploaded document management
7. **reports** - Generated compliance reports
8. **audit_logs** - System audit trail
9. **sanctions_lists** - Sanctions database

## 🔧 Configuration

### Environment Variables

```bash
FLASK_ENV=production          # Environment mode
SECRET_KEY=your-secret-key    # Flask secret key
UPLOAD_FOLDER=uploads/        # File upload directory
MAX_CONTENT_LENGTH=524288000  # Max upload size (500MB)
```

### Database Location

- **Local:** `aml_multi_user.db` (auto-created)
- **Production:** Configure in `config.py`

## 📚 Documentation

- [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - Complete API reference
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Cloud deployment instructions
- [QUICK_START.md](QUICK_START.md) - Beginner's guide
- [README_v3.5.md](README_v3.5.md) - Version history

## 👥 Multi-User Support

- Create multiple user accounts
- Each user sees only their cases
- Role-based access (analyst, manager, admin)
- Full user management system

## 🤖 AI Features

- Automatic risk scoring (0-100)
- Risk factor analysis:
  - Transaction Velocity
  - Geographic Risk
  - Sanctions Match
  - Structuring Patterns
  - PEP Connections
- ML-based recommendations
- Threat level assessment

## 📱 Frontend Features

- **Responsive Design** - Works on mobile and desktop
- **Real-Time Search** - Instant case/transaction search
- **Interactive Dashboard** - Stats and quick actions
- **Form Validation** - Client-side and server-side
- **Notifications** - Real-time user feedback
- **Edit/Delete/View** - Full CRUD operations

## 🐛 Troubleshooting

### Server won't start

```bash
# Check if port 5000 is in use
netstat -ano | findstr ":5000"

# Kill process using port
taskkill /PID <PID> /F
```

### ngrok connection failed

```bash
# Ensure Flask is running first
python start_server.py

# Then run ngrok in another terminal
ngrok http 5000
```

### Login not working from remote device

- Check your ngrok URL is correct
- Ensure CORS is enabled (it is by default)
- Verify username and password

## 📦 Dependencies

See [requirements.txt](requirements.txt) for full list:

- Flask 2.3.7
- Flask-CORS 3.0.10
- Werkzeug 2.3.7
- SQLAlchemy (via dependencies)
- PyPDF2
- python-docx
- openpyxl
- nltk
- textblob
- numpy
- pytesseract

## 📄 License

This project is proprietary software. All rights reserved.

## 👨‍💼 Author

**Waqas Khan Niazi**

Professional AML Compliance Software Developer

## 📞 Support

For issues and questions:

1. Check [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
2. Review [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
3. Check existing GitHub Issues
4. Create a new Issue with detailed description

## 🎯 Roadmap

- [ ] Mobile app (React Native)
- [ ] Advanced analytics dashboard
- [ ] Machine learning model improvements
- [ ] Blockchain integration for immutable records
- [ ] Real-time threat intelligence feeds
- [ ] Multi-language support
- [ ] Advanced reporting engine

## 🙏 Acknowledgments

- Built with Flask
- Charts by Chart.js
- Icons and design inspired by modern compliance platforms

---

**Version:** 9.0  
**Last Updated:** February 2, 2026  
**Status:** Production Ready ✅
