# AML Case Management System v10.0+ - Enhanced Features

## 🎉 NEW: Complete Enquiry/Inquiry Management System

The system now includes comprehensive enquiry management with full CRUD operations, advanced search, and complete audit trail tracking.

---

## 📋 Enquiry Management Features

### 1. **Create Enquiries**

- Create new enquiries/inquiries with detailed information
- Automatic enquiry numbering (ENQ-YYYYMMDD-XXXXXXXX)
- Link enquiries to cases
- Set priority levels (LOW, MEDIUM, HIGH, CRITICAL)
- Categorize enquiries
- Track source of enquiry (MANUAL, EMAIL, PHONE, AUTOMATED, etc.)

### 2. **View & Retrieve Enquiries**

- Get all enquiries for a user
- Filter by status (OPEN, IN_PROGRESS, ON_HOLD, CLOSED, RESOLVED, ESCALATED)
- Get detailed enquiry information
- View enquiry history and timeline

### 3. **Edit Enquiries**

- Update enquiry fields
- Modify subject, description, category
- Update priority levels
- Attach documents and references

### 4. **Update Status**

- OPEN → IN_PROGRESS → CLOSED
- Hold enquiries (ON_HOLD)
- Mark as RESOLVED
- Escalate if needed
- Automatic timestamp tracking for status changes

### 5. **Add Findings**

- Document findings for each enquiry
- Add investigation results
- Track changes to findings

### 6. **Add Recommendations**

- Record recommendations based on findings
- Update recommendations as inquiry progresses

### 7. **Delete/Archive Enquiries**

- Soft delete (mark as DELETED, don't remove from DB)
- Maintains audit trail
- Recoverable if needed

### 8. **Assign Enquiries**

- Assign to team members
- Change assignments
- Track who owns each enquiry

### 9. **Search Enquiries**

- Search by text (subject, description, enquiry number)
- Filter by:
  - Status
  - Priority
  - Category
  - Linked case
  - Date range
  - Assigned user

### 10. **Trace/Audit Trail**

- Complete action history
- Who created, updated, and resolved enquiry
- When changes were made
- What was changed
- IP address tracking for compliance

### 11. **Statistics & Reporting**

- Total enquiries count
- Breakdown by status
- Breakdown by priority
- Breakdown by category
- Performance metrics

### 12. **Bulk Operations**

- Update multiple enquiries at once
- Bulk status changes
- Bulk assignments
- Bulk categorization

---

## 🔌 API Endpoints

### Enquiry CRUD Operations

#### Create Enquiry

```
POST /api/enquiries/create
Content-Type: application/json

{
  "subject": "Suspicious transaction detected",
  "description": "Large international transfer",
  "category": "TRANSACTION",
  "priority": "HIGH",
  "case_id": "optional-case-id",
  "source": "MANUAL"
}

Response:
{
  "success": true,
  "enquiry_id": "uuid",
  "enquiry_number": "ENQ-20260201-XXXXXXXX",
  "message": "Enquiry created successfully"
}
```

#### Get All Enquiries

```
GET /api/enquiries
GET /api/enquiries?status=OPEN

Response:
{
  "enquiries": [
    {
      "id": "uuid",
      "enquiry_number": "ENQ-20260201-XXXXXXXX",
      "subject": "...",
      "status": "OPEN",
      "priority": "HIGH",
      ...
    }
  ],
  "count": 5
}
```

#### Get Single Enquiry

```
GET /api/enquiries/<enquiry_id>

Response:
{
  "id": "uuid",
  "enquiry_number": "ENQ-20260201-XXXXXXXX",
  "subject": "Suspicious transaction detected",
  "description": "Large international transfer",
  "category": "TRANSACTION",
  "priority": "HIGH",
  "status": "OPEN",
  "assigned_to": "user-id",
  "findings": null,
  "recommendations": null,
  "created_at": "2026-02-01 21:50:00",
  "updated_at": "2026-02-01 21:50:00",
  "resolved_at": null
}
```

### Enquiry Edit & Update

#### Edit Enquiry

```
PUT /api/enquiries/<enquiry_id>/edit
Content-Type: application/json

{
  "subject": "Updated subject",
  "description": "Updated description",
  "category": "UPDATED_CATEGORY"
}

Response:
{
  "success": true,
  "message": "Enquiry updated successfully"
}
```

#### Update Status

```
PUT /api/enquiries/<enquiry_id>/status
Content-Type: application/json

{
  "status": "IN_PROGRESS"
}

Valid statuses: OPEN, IN_PROGRESS, ON_HOLD, CLOSED, RESOLVED, ESCALATED

Response:
{
  "success": true,
  "message": "Status updated to IN_PROGRESS"
}
```

#### Add Findings

```
PUT /api/enquiries/<enquiry_id>/findings
Content-Type: application/json

{
  "findings": "Detailed findings from investigation..."
}

Response:
{
  "success": true,
  "message": "Findings added successfully"
}
```

#### Add Recommendations

```
PUT /api/enquiries/<enquiry_id>/recommendations
Content-Type: application/json

{
  "recommendations": "Recommended actions..."
}

Response:
{
  "success": true,
  "message": "Recommendations added successfully"
}
```

#### Assign Enquiry

```
PUT /api/enquiries/<enquiry_id>/assign
Content-Type: application/json

{
  "assigned_to": "user-id"
}

Response:
{
  "success": true,
  "message": "Enquiry assigned successfully"
}
```

### Enquiry Delete

#### Delete Enquiry (Soft Delete)

```
DELETE /api/enquiries/<enquiry_id>/delete

Response:
{
  "success": true,
  "message": "Enquiry deleted successfully"
}
```

### Enquiry Search & Query

#### Search Enquiries

```
POST /api/enquiries/search
Content-Type: application/json

{
  "query": "suspicious",
  "filters": {
    "status": "OPEN",
    "priority": "HIGH",
    "category": "TRANSACTION",
    "case_id": "optional"
  }
}

Response:
{
  "results": [...],
  "count": 3
}
```

#### Get Enquiry History

```
GET /api/enquiries/<enquiry_id>/history

Response:
{
  "history": [
    {
      "timestamp": "2026-02-01 21:50:00",
      "action": "CREATED",
      "description": "Enquiry created with subject: ..."
    },
    {
      "timestamp": "2026-02-01 21:55:00",
      "action": "UPDATED",
      "description": "Enquiry updated - Status: IN_PROGRESS"
    }
  ]
}
```

### Bulk Operations

#### Bulk Update Enquiries

```
POST /api/enquiries/bulk/update
Content-Type: application/json

{
  "enquiry_ids": ["id1", "id2", "id3"],
  "updates": {
    "status": "IN_PROGRESS",
    "priority": "HIGH",
    "assigned_to": "user-id"
  }
}

Response:
{
  "results": [
    {"enquiry_id": "id1", "status": "updated", "message": "..."},
    {"enquiry_id": "id2", "status": "updated", "message": "..."},
    {"enquiry_id": "id3", "status": "updated", "message": "..."}
  ]
}
```

### Statistics

#### Get Enquiry Statistics

```
GET /api/enquiries/statistics

Response:
{
  "total": 25,
  "by_status": {
    "OPEN": 10,
    "IN_PROGRESS": 8,
    "ON_HOLD": 2,
    "RESOLVED": 5,
    "CLOSED": 0
  },
  "by_priority": {
    "LOW": 5,
    "MEDIUM": 10,
    "HIGH": 8,
    "CRITICAL": 2
  },
  "by_category": {
    "TRANSACTION": 12,
    "CUSTOMER": 8,
    "DOCUMENTATION": 5
  }
}
```

---

## 📊 Case Management Enhancements

All existing case management features are still available and enhanced:

### Case CRUD Operations

- **Create Cases** - `POST /api/cases/create`
- **List Cases** - `GET /api/cases`
- **Get Case** - `GET /api/cases/<case_id>`
- **Edit Case** - `PUT /api/cases/<case_id>/edit`
- **Update Case** - `POST /api/cases/<case_id>/update`
- **Delete Case** - `DELETE /api/cases/<case_id>/delete`
- **Restore Case** - `POST /api/cases/<case_id>/restore`

### Case Search & Analysis

- **Search Cases** - `POST /api/search/cases`
- **Advanced Search** - `POST /api/search/advanced`
- **AI Assessment** - `POST /api/assess/<case_id>`
- **Case Comparison** - `POST /api/analytics/comparison`

### Case Bulk Operations

- **Bulk Update** - `POST /api/cases/bulk/update`
- **Bulk Delete** - `POST /api/cases/bulk/delete`
- **Bulk Status Update** - `POST /api/cases/bulk/status`

### Case Audit & Compliance

- **Get Audit Trail** - `GET /api/audit/<case_id>`
- **Get Case History** - `GET /api/trace/<case_id>`
- **Compliance Report** - `POST /api/compliance`

---

## 🗂️ Database Schema

### Enquiries Table

```sql
CREATE TABLE enquiries (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  case_id TEXT,
  enquiry_number TEXT UNIQUE,
  subject TEXT NOT NULL,
  description TEXT,
  category TEXT,
  priority TEXT DEFAULT 'MEDIUM',
  status TEXT DEFAULT 'OPEN',
  assigned_to TEXT,
  source TEXT,
  reference_documents TEXT,
  findings TEXT,
  recommendations TEXT,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  resolved_at TIMESTAMP
)
```

### Status Values

- OPEN - New enquiry
- IN_PROGRESS - Being investigated
- ON_HOLD - Temporarily halted
- CLOSED - Investigation complete
- RESOLVED - Issue resolved
- ESCALATED - Escalated to senior management
- DELETED - Soft deleted

### Priority Values

- LOW
- MEDIUM
- HIGH
- CRITICAL

---

## 🔒 Audit Trail & Compliance

Every action is logged:

- **Action Type**: ENQUIRY_CREATE, ENQUIRY_EDIT, ENQUIRY_STATUS_UPDATE, etc.
- **Entity Type**: ENQUIRY
- **Entity ID**: enquiry_id
- **Old Value**: Previous state
- **New Value**: New state
- **User ID**: Who made the change
- **Timestamp**: When it happened
- **IP Address**: Where it came from
- **Details**: Additional context

---

## 📈 Performance & Analytics

### Enquiry Statistics Available

1. **Total Enquiries** - Count of all enquiries
2. **By Status** - Breakdown of enquiries by status
3. **By Priority** - Distribution of priorities
4. **By Category** - Categorization breakdown
5. **Assignment Status** - Who has which enquiries
6. **Resolution Time** - Average time to resolve
7. **Activity Timeline** - Historical trends

---

## 💡 Use Cases

### Scenario 1: Suspicious Transaction

1. Create enquiry with HIGH priority
2. Link to case if applicable
3. Assign to analyst
4. Add findings as investigation progresses
5. Update status to IN_PROGRESS
6. Add recommendations
7. Mark as RESOLVED

### Scenario 2: Bulk Compliance Check

1. Search for all OPEN enquiries
2. Bulk update status to IN_PROGRESS
3. Bulk assign to compliance team
4. Track progress via statistics

### Scenario 3: Complex Investigation

1. Create parent enquiry
2. Create related enquiries for sub-issues
3. Link all to same case
4. Cross-reference findings
5. Generate consolidated report

---

## 🚀 Integration Examples

### JavaScript/Frontend

```javascript
// Create enquiry
const response = await fetch('/api/enquiries/create', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    subject: 'Suspicious activity',
    category: 'TRANSACTION',
    priority: 'HIGH'
  })
});

// Search enquiries
const searchResults = await fetch('/api/enquiries/search', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    query: 'suspicious',
    filters: {status: 'OPEN'}
  })
});

// Update status
await fetch('/api/enquiries/<id>/status', {
  method: 'PUT',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({status: 'IN_PROGRESS'})
});
```

### Python/Backend

```python
import requests

# Create enquiry
resp = requests.post('http://localhost:5000/api/enquiries/create', json={
    'subject': 'Investigation needed',
    'category': 'CUSTOMER',
    'priority': 'MEDIUM'
})

# Get statistics
stats = requests.get('http://localhost:5000/api/enquiries/statistics').json()
print(f"Total enquiries: {stats['total']}")
```

---

## ✨ Key Features Summary

✅ **Complete CRUD Operations** - Create, Read, Update, Delete enquiries  
✅ **Status Management** - 6 different status states  
✅ **Priority Tracking** - 4 priority levels  
✅ **Assignment System** - Assign to team members  
✅ **Findings & Recommendations** - Document investigation results  
✅ **Search & Filtering** - Multi-criteria search  
✅ **Audit Trail** - Complete compliance logging  
✅ **Bulk Operations** - Manage multiple enquiries  
✅ **Statistics & Analytics** - Monitor enquiry metrics  
✅ **Case Linking** - Connect enquiries to cases  
✅ **History Tracking** - View complete timeline  
✅ **Source Tracking** - Know where enquiry came from  

---

**System Version: v10.0+**  
**Status: Production Ready** ✅  
**All Features Active**
