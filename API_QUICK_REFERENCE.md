# 🚀 AML v10.0 - QUICK API REFERENCE

## NEW CAPABILITIES

### 🔍 AUDIT & TRACE

```
GET  /api/audit/trail          → View who did what, when, where
GET  /api/audit/trace/<id>     → Complete history of changes
```

### 🔎 SEARCH EVERYTHING

```
POST /api/search               → Basic + Advanced multi-criteria search
POST /api/search/transactions/<cid> → Find suspicious transactions
```

### ⚡ BULK OPERATIONS

```
POST /api/cases/bulk/update    → Update 100+ cases at once
POST /api/cases/bulk/delete    → Delete multiple cases
POST /api/cases/bulk/status    → Change status in bulk
```

### ✏️ EDIT & MANAGE

```
PUT  /api/cases/<id>/edit      → Update case details
DELETE /api/cases/<id>/delete  → Delete case (with audit)
POST /api/cases/<id>/restore   → Undo deletion
```

### 💰 TRANSACTION OPS

```
PUT  /api/transactions/<id>/edit    → Modify transaction
DELETE /api/transactions/<id>/delete → Remove transaction
GET  /api/transactions/<cid>/list   → List all in case
```

### 📊 ANALYTICS

```
GET  /api/analytics/dashboard  → Dashboard overview
POST /api/analytics/comparison → Compare cases side-by-side
```

---

## 💡 EXAMPLE REQUESTS

### Search Cases

```json
POST /api/search
{
  "type": "advanced",
  "criteria": {
    "client_name": "Company Name",
    "min_risk": 70,
    "status": "pending",
    "country": "US"
  }
}
```

### Bulk Update

```json
POST /api/cases/bulk/update
{
  "case_ids": ["case1", "case2", "case3"],
  "updates": {
    "status": "approved",
    "risk_level": "MEDIUM"
  }
}
```

### Edit Case

```json
PUT /api/cases/ABC123/edit
{
  "client_name": "New Name",
  "status": "investigating",
  "notes": "Updated findings"
}
```

### View Audit Trail

```
GET /api/audit/trail?entity_id=ABC123&action=CASE_EDIT&limit=50
```

---

## ✨ KEY FEATURES

- **COMPLETE TRACEABILITY** - Every action logged with user, IP, timestamp
- **BULK OPERATIONS** - Process 100s of cases instantly  
- **ADVANCED SEARCH** - Filter by 10+ criteria
- **CASE RESTORATION** - Recover accidental deletions
- **COMPLIANCE READY** - Full audit trail for regulators
- **IMMUTABLE LOG** - Cannot be tampered with
- **IP TRACKING** - Know who accessed from where

---

## 🔐 ALL CHANGES ARE TRACKED

Every action creates an audit record with:

- ✅ WHO made the change (user_id)
- ✅ WHAT changed (old_value → new_value)  
- ✅ WHEN it happened (timestamp)
- ✅ WHERE from (ip_address)
- ✅ WHY/CONTEXT (action type)

---

## 🎯 AUDIT ACTIONS TRACKED

- `CASE_CREATE` - New case created
- `CASE_EDIT` - Case information updated
- `CASE_DELETE` - Case deleted
- `CASE_RESTORE` - Case restored from trash
- `TRANSACTION_EDIT` - Transaction modified
- `TRANSACTION_DELETE` - Transaction removed
- `BULK_UPDATE` - Multiple items updated
- `BULK_DELETE` - Multiple items deleted

---

**System**: AML Case Management v10.0  
**Enhanced**: 2026-02-01  
**Status**: ✅ PRODUCTION READY
