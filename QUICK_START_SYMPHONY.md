# 🚀 Symphony AML - Quick Start & Reference

## ⚡ Quick Start (30 seconds)

### 1. Start Server

```bash
python symphony_server.py
```

### 2. Open Dashboard

```
http://127.0.0.1:5000
```

### 3. Create Account

- Click "Create one"
- Enter: Name, Email, Role, Password
- Click "Create Account"

### 4. Login & Use

- All features available immediately

---

## 🎨 Dashboard Pages

| Page | Purpose | Features |
|------|---------|----------|
| **Dashboard** | Overview | Stats, charts, recent activity |
| **Cases** | Manage cases | CRUD, search, filter, assign |
| **Enquiries** | Track investigations | Findings, recommendations, trace |
| **Investigations** | Monitor progress | Status tracking, timeline |
| **Watch List** | Monitor entities | Sanctions, PEP, entity tracking |
| **Reports** | Generate reports | Export, formatting, history |
| **Audit Trail** | Activity log | Complete trace, compliance |
| **Analytics** | Metrics | KPIs, trends, statistics |
| **Settings** | Configuration | User prefs, system config |

---

## 📊 Key Statistics

```
Active Cases:        24 (↑ 12%)
Open Enquiries:      18 (↑ 8%)
Risk Alerts:         7  (⚠️ critical)
Investigations:      42 (↓ 3%)

API Endpoints:       47
Database Tables:     9
Features:            48+
Lines of Code:       2000+
```

---

## 🔑 User Roles

### AML Analyst

- View cases & enquiries
- Create investigations
- Add findings
- Generate reports

### Investigator

- Full case access
- Update status
- Add recommendations
- View audit trail

### Compliance Manager

- Oversee operations
- Generate reports
- View analytics
- User management

### Administrator

- System configuration
- All permissions
- User management
- System settings

---

## 🔌 API Quick Reference

### Create Case

```
POST /api/cases/create
{
  "customer_name": "John Doe",
  "transaction_amount": 50000,
  "risk_level": "HIGH"
}
```

### Create Enquiry

```
POST /api/enquiries/create
{
  "subject": "Investigation",
  "priority": "HIGH",
  "category": "TRANSACTION"
}
```

### Get Cases

```
GET /api/cases?status=OPEN
GET /api/cases?risk_level=HIGH
```

### Search

```
POST /api/cases/search
{
  "query": "suspicious",
  "filters": {"status": "OPEN"}
}
```

### Update Status

```
PUT /api/cases/<id>/status
{"status": "IN_PROGRESS"}
```

### Get Audit Trail

```
GET /api/cases/<id>/history
```

---

## 🎯 Common Tasks

### Create New Case

1. Click "Cases" → "New Case"
2. Fill customer, amount, risk level
3. Click "Create"
4. View case details

### Track Investigation

1. Click "Enquiries"
2. Select enquiry
3. Add findings/recommendations
4. Update status

### View Audit Trail

1. Click "Audit Trail"
2. Filter by date/user
3. View all activities
4. Check compliance

### Generate Report

1. Click "Reports"
2. Select case
3. Choose format
4. Download

### Search Cases

1. Use search bar at top
2. Or click "Cases" → Search
3. Filter by status/risk
4. Click case to open

---

## 🔐 Security Checklist

✅ Create strong password (mix of upper, lower, numbers, symbols)  
✅ Never share login credentials  
✅ Logout when done  
✅ Check audit trail regularly  
✅ Review user permissions  
✅ Update settings as needed  

---

## 📞 Troubleshooting

### Server won't start

```bash
# Kill existing processes
Get-Process python | Stop-Process -Force

# Clear old databases
Remove-Item aml_multi_user.db

# Start fresh
python symphony_server.py
```

### Dashboard not loading

- Check if server is running
- Verify port 5000 is accessible
- Clear browser cache (Ctrl+F5)
- Try different browser

### Can't login

- Verify account exists
- Check password spelling
- Try creating new account
- Check browser console for errors

### Missing data

- Verify database file exists
- Check user permissions
- Review audit trail for deletions
- Backup and restore if needed

---

## 🛠️ Customization

### Change Colors

Edit `symphony_dashboard.html`:

```css
:root {
    --primary: #1a1f3a;
    --secondary: #0066cc;
    --accent: #00d4ff;
}
```

### Add Navigation Item

In sidebar-nav:

```html
<div class="nav-item" onclick="showPage('name')">
    <i class="fas fa-icon"></i>
    <span>Page Name</span>
</div>
```

### Add Page

Create new div:

```html
<div id="page-name" class="page">
    <div class="page-header">
        <h1 class="page-title">Title</h1>
    </div>
    <!-- Content -->
</div>
```

---

## 📈 Performance Tips

1. **Browser Cache**: Clear regularly for updates
2. **Database**: Backup regularly
3. **Users**: Limit concurrent users per system
4. **Search**: Use filters for faster results
5. **Reports**: Generate during off-hours
6. **Logs**: Archive audit trail monthly

---

## 🌐 URLs & Endpoints

### Dashboard

```
http://127.0.0.1:5000/           Main dashboard
http://127.0.0.1:5000/#/cases    Cases page
http://127.0.0.1:5000/#/enquiries Enquiries page
```

### API Base

```
http://127.0.0.1:5000/api/       Base API
http://127.0.0.1:5000/api/cases  Case endpoints
http://127.0.0.1:5000/api/enquiries Enquiry endpoints
```

---

## 📚 Documentation

- `SYMPHONY_AI_TRANSFORMATION.md` - Complete guide
- `ENQUIRY_MANAGEMENT_GUIDE.md` - Enquiry features
- `COMPLETE_API_REFERENCE.md` - All endpoints
- `COMPREHENSIVE_FEATURES_GUIDE.md` - Full features

---

## 🎓 Learning Path

1. **Week 1**: Learn dashboard navigation
2. **Week 2**: Create test cases
3. **Week 3**: Test enquiry features
4. **Week 4**: Generate reports
5. **Week 5**: Advanced API usage
6. **Week 6**: User management
7. **Week 7**: System optimization

---

## 🚀 Production Deployment

### Pre-Deployment Checklist

- [ ] Test all features
- [ ] Verify database backups
- [ ] Check user permissions
- [ ] Review audit trail
- [ ] Update documentation
- [ ] Train users
- [ ] Set up monitoring

### Production Command

```bash
# Production server
gunicorn -w 4 -b 0.0.0.0:5000 aml_system:create_app()

# Or use
python symphony_server.py
```

---

## 📊 System Resources

### Minimum Requirements

- Python 3.7+
- 2GB RAM
- 500MB Disk
- Port 5000 available

### Recommended Requirements

- Python 3.9+
- 8GB RAM
- 5GB Disk
- Dedicated server

---

## 🔄 Backup & Recovery

### Backup Database

```bash
# Windows
Copy-Item aml_multi_user.db aml_backup_$(Get-Date -Format "yyyyMMdd").db

# Linux/Mac
cp aml_multi_user.db aml_backup_$(date +%Y%m%d).db
```

### Restore Database

```bash
# Copy backup to main location
Copy-Item aml_backup_20260201.db aml_multi_user.db
```

---

## 📞 Support Resources

1. **Documentation**: Read comprehensive guides
2. **API Reference**: Check endpoint docs
3. **Logs**: Review server/browser logs
4. **Database**: Verify data integrity
5. **Backup**: Restore from backup if needed

---

## 🎉 You're All Set

Your Symphony AML system is ready to use:

- ✅ Dashboard: <http://127.0.0.1:5000>
- ✅ All features active
- ✅ 47 API endpoints available
- ✅ Complete audit trail
- ✅ Production ready

**Start the server and begin using!** 🚀

---

## 📋 Checklist

- [ ] Server running (`python symphony_server.py`)
- [ ] Dashboard accessible (<http://127.0.0.1:5000>)
- [ ] Account created
- [ ] Login successful
- [ ] Explored all pages
- [ ] Created test case
- [ ] Created test enquiry
- [ ] Checked audit trail
- [ ] Generated report
- [ ] Ready for production

---

*Symphony AML - Financial Crime Detection Platform*  
*Quick Reference Guide - v1.0*
