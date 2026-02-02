# AML System - Complete API Reference v10.0+

## 📡 Total API Endpoints: 45+

---

## 🔐 Authentication Routes

### Register User

```
POST /api/auth/register
{
  "username": "string",
  "email": "string",
  "password": "string",
  "full_name": "string",
  "organization": "string"
}
```

### Login

```
POST /api/auth/login
{
  "username": "string",
  "password": "string"
}
```

### Logout

```
POST /api/auth/logout
```

### Get Profile

```
GET /api/auth/profile
```

---

## 📋 Case Management (7 Core Routes)

### Create Case

```
POST /api/cases/create
{
  "title": "string",
  "category": "string",
  "description": "string",
  "amount": number,
  "risk_level": "LOW|MEDIUM|HIGH|CRITICAL",
  "accused_names": "string"
}
```

### List Cases

```
GET /api/cases
```

### Get Case Details

```
GET /api/cases/<case_id>
```

### Edit Case

```
PUT /api/cases/<case_id>/edit
{
  "title": "string",
  "category": "string",
  "description": "string",
  "status": "OPEN|UNDER_REVIEW|CLOSED"
}
```

### Update Case

```
POST /api/cases/<case_id>/update
{
  "field": "value"
}
```

### Delete Case (Soft Delete)

```
DELETE /api/cases/<case_id>/delete
```

### Restore Case

```
POST /api/cases/<case_id>/restore
```

---

## 🔍 Case Bulk Operations (3 Routes)

### Bulk Update Cases

```
POST /api/cases/bulk/update
{
  "case_ids": ["id1", "id2"],
  "updates": {
    "status": "IN_REVIEW",
    "risk_level": "HIGH"
  }
}
```

### Bulk Delete Cases

```
POST /api/cases/bulk/delete
{
  "case_ids": ["id1", "id2"]
}
```

### Bulk Status Update

```
POST /api/cases/bulk/status
{
  "case_ids": ["id1", "id2"],
  "status": "CLOSED"
}
```

---

## 🔬 AI Assessment Routes (2 Routes)

### Assess Case

```
POST /api/assess/<case_id>
```

### Get Assessment

```
GET /api/assess/<case_id>
```

---

## 📄 Document Management (3 Routes)

### Upload Document

```
POST /api/documents/<case_id>/upload
Form data with file
```

### Analyze Documents

```
POST /api/analyze-documents/<case_id>
```

### Get Documents

```
GET /api/documents/<case_id>
```

---

## 🔍 Search & Query Routes (3 Routes)

### Search Cases

```
POST /api/search/cases
{
  "query": "string",
  "filters": {
    "status": "string",
    "risk_level": "string"
  }
}
```

### Search Transactions

```
POST /api/search/transactions
{
  "query": "string",
  "filters": {}
}
```

### Advanced Search

```
POST /api/search/advanced
{
  "query": "string",
  "filters": {}
}
```

---

## 📊 Audit & Compliance Routes (3 Routes)

### Get Audit Trail

```
GET /api/audit/<case_id>
```

### Get Case Trace (History)

```
GET /api/trace/<case_id>
```

### Compliance Report

```
POST /api/compliance
```

---

## 💼 NEW: Enquiry Management Routes (11 Routes)

### Create Enquiry

```
POST /api/enquiries/create
{
  "subject": "string",
  "description": "string",
  "category": "string",
  "priority": "LOW|MEDIUM|HIGH|CRITICAL",
  "case_id": "optional-id",
  "source": "string"
}
```

### List Enquiries

```
GET /api/enquiries
GET /api/enquiries?status=OPEN
```

### Get Enquiry Details

```
GET /api/enquiries/<enquiry_id>
```

### Edit Enquiry

```
PUT /api/enquiries/<enquiry_id>/edit
{
  "subject": "string",
  "description": "string"
}
```

### Update Status

```
PUT /api/enquiries/<enquiry_id>/status
{
  "status": "OPEN|IN_PROGRESS|ON_HOLD|CLOSED|RESOLVED|ESCALATED"
}
```

### Add Findings

```
PUT /api/enquiries/<enquiry_id>/findings
{
  "findings": "string"
}
```

### Add Recommendations

```
PUT /api/enquiries/<enquiry_id>/recommendations
{
  "recommendations": "string"
}
```

### Assign Enquiry

```
PUT /api/enquiries/<enquiry_id>/assign
{
  "assigned_to": "user-id"
}
```

### Delete Enquiry

```
DELETE /api/enquiries/<enquiry_id>/delete
```

### Search Enquiries

```
POST /api/enquiries/search
{
  "query": "string",
  "filters": {
    "status": "string",
    "priority": "string"
  }
}
```

### Get Enquiry History

```
GET /api/enquiries/<enquiry_id>/history
```

### Bulk Update Enquiries

```
POST /api/enquiries/bulk/update
{
  "enquiry_ids": ["id1", "id2"],
  "updates": {}
}
```

### Enquiry Statistics

```
GET /api/enquiries/statistics
```

---

## 💰 Transaction Routes (3 Routes)

### Create Transaction

```
POST /api/transactions/<case_id>/create
{
  "date": "YYYY-MM-DD",
  "amount": number,
  "currency": "USD",
  "type": "DEBIT|CREDIT",
  "description": "string"
}
```

### Get Transactions

```
GET /api/transactions/<case_id>
```

### Delete Transaction

```
DELETE /api/transactions/<txn_id>/delete
```

---

## 📈 Analytics Routes (2 Routes)

### Dashboard Analytics

```
GET /api/analytics/dashboard
```

### Case Comparison

```
POST /api/analytics/comparison
{
  "case_ids": ["id1", "id2"]
}
```

---

## 📃 Report Routes (2 Routes)

### Generate Report

```
POST /api/report/<case_id>
```

### Get Report

```
GET /api/report/<case_id>
```

---

## 🏠 Main Routes (1 Route)

### Dashboard

```
GET /
```

---

## 📊 Endpoint Summary by Category

| Category | Endpoints | New |
|----------|-----------|-----|
| Authentication | 4 | - |
| Case Management | 7 | - |
| Case Bulk Ops | 3 | - |
| AI Assessment | 2 | - |
| Documents | 3 | - |
| Search | 3 | - |
| Audit & Compliance | 3 | - |
| **Enquiry Management** | **13** | **✅** |
| Transactions | 3 | - |
| Analytics | 2 | - |
| Reports | 2 | - |
| Main | 1 | - |
| **TOTAL** | **47** | **13 NEW** |

---

## 🔑 Authentication

All endpoints except `/api/auth/register`, `/api/auth/login`, and `/` require authentication.

**Session-based authentication:**

- User must be logged in
- `user_id` stored in session
- Session cookie automatically managed

**Headers Required:**

```
Content-Type: application/json
```

**Session Check:**
All protected endpoints check:

```python
if 'user_id' not in session:
    return {'error': 'Not authenticated'}, 401
```

---

## 🔄 Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK - Success |
| 201 | Created - New resource created |
| 400 | Bad Request - Invalid input |
| 401 | Unauthorized - Not authenticated |
| 404 | Not Found - Resource doesn't exist |
| 500 | Server Error |

---

## 📋 Common Request/Response Patterns

### Success Response

```json
{
  "success": true,
  "message": "Operation completed",
  "data": {}
}
```

### Error Response

```json
{
  "success": false,
  "error": "Error message",
  "message": "Error message"
}
```

### List Response

```json
{
  "items": [],
  "count": 0,
  "total": 0
}
```

---

## 🔒 Audit Trail Logging

Every action is logged with:

- Action type (CREATE, EDIT, DELETE, etc.)
- Entity type (CASE, ENQUIRY, etc.)
- Entity ID
- Old values
- New values
- User ID
- Timestamp
- IP address
- Additional details

---

## 💾 Data Retention

- Cases: Indefinite (soft delete only)
- Enquiries: Indefinite (soft delete only)
- Transactions: Indefinite
- Audit Trail: Indefinite (compliance requirement)
- Sessions: Until logout

---

## 🚀 Quick Start

### 1. Register

```
POST /api/auth/register
```

### 2. Login

```
POST /api/auth/login
```

### 3. Create Case

```
POST /api/cases/create
```

### 4. Create Enquiry

```
POST /api/enquiries/create
```

### 5. Search & Analyze

```
POST /api/search/cases
POST /api/assess/<case_id>
```

### 6. Track & Audit

```
GET /api/audit/<case_id>
GET /api/enquiries/statistics
```

---

## 🔗 Related Documentation

- [ENQUIRY_MANAGEMENT_GUIDE.md](ENQUIRY_MANAGEMENT_GUIDE.md) - Detailed enquiry features
- [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - Legacy API docs
- [README.md](README.md) - System overview
- [GETTING_STARTED.md](GETTING_STARTED.md) - Quick start guide

---

**API Version: v10.0+**  
**Last Updated: February 1, 2026**  
**Status: Production Ready** ✅
