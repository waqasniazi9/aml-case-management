# AML AML Case Management System - API Documentation

## Base URL

```
http://localhost:5000/api
```

## Authentication

Include JWT token in header for authenticated endpoints:

```
Authorization: Bearer <token>
```

---

## Endpoints

### 1. Health Check

**Check if API is running**

- **Method:** GET
- **Endpoint:** `/health`
- **Auth Required:** No
- **Response:**

```json
{
  "status": "healthy",
  "timestamp": "2024-01-31T10:30:00",
  "version": "3.0"
}
```

---

### 2. Create Case

**Create a new AML investigation case**

- **Method:** POST
- **Endpoint:** `/cases`
- **Auth Required:** Yes
- **Request Headers:**

```
Content-Type: application/json
Authorization: Bearer <token>
```

- **Request Body:**

```json
{
  "enquiry_number": "001/2024",
  "date_created": "2024-01-31",
  "source": "FMU",
  "category": "STR",
  "accused_names": ["Sample Subject A", "Sample Subject B"],
  "cnic_numbers": ["00000-0000000-0", "00000-0000000-1"],
  "allegation_summary": "Sample suspicious transaction pattern for testing",
  "amount_pkr": 2500000,
  "sensitivity_level": "high"
}
```

- **Response:** (201 Created)

```json
{
  "success": true,
  "message": "Case created successfully",
  "case_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

- **Error Response:** (400 Bad Request)

```json
{
  "success": false,
  "message": "Missing required fields"
}
```

---

### 3. List Cases

**Retrieve paginated list of cases**

- **Method:** GET
- **Endpoint:** `/cases?limit=50&offset=0`
- **Auth Required:** Yes
- **Query Parameters:**
  - `limit` (optional, default: 50) - Number of cases per page
  - `offset` (optional, default: 0) - Number of cases to skip
  - `status` (optional) - Filter by status
  - `priority` (optional) - Filter by priority

- **Response:** (200 OK)

```json
{
  "count": 5,
  "cases": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "enquiry_number": "123/2024",
      "date_created": "2024-01-31",
      "source": "FMU",
      "category": "STR",
      "accused_names": ["Sample Subject A"],
      "cnic_numbers": ["00000-0000000-0"],
      "allegation_summary": "Suspicious transactions",
      "amount_pkr": 2500000,
      "sensitivity_level": "high",
      "status": "pending",
      "priority": "medium",
      "risk_score": 78,
      "assigned_officer": "Sample Officer",
      "created_at": "2024-01-31T10:30:00",
      "updated_at": "2024-01-31T10:30:00"
    }
  ]
}
```

---

### 4. Get Case Details

**Retrieve specific case information**

- **Method:** GET
- **Endpoint:** `/cases/<case_id>`
- **Auth Required:** Yes
- **Response:** (200 OK)

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "enquiry_number": "123/2024",
  "date_created": "2024-01-31",
  "source": "FMU",
  "category": "STR",
  "accused_names": ["Sample Subject A"],
  "cnic_numbers": ["00000-0000000-0"],
  "allegation_summary": "Suspicious transactions",
  "amount_pkr": 2500000,
  "sensitivity_level": "high",
  "status": "pending",
  "priority": "medium",
  "risk_score": 78,
  "assigned_officer": "Sample Officer",
  "documents": [],
  "notes": [],
  "created_at": "2024-01-31T10:30:00",
  "updated_at": "2024-01-31T10:30:00"
}
```

- **Error Response:** (404 Not Found)

```json
{
  "error": "Case not found"
}
```

---

### 5. Update Case

**Update existing case information**

- **Method:** PUT
- **Endpoint:** `/cases/<case_id>`
- **Auth Required:** Yes
- **Request Body:** (partial update)

```json
{
  "status": "under_probe",
  "priority": "high",
  "assigned_officer": "Sample Officer",
  "risk_score": 85,
  "notes": [
    {
      "timestamp": "2024-01-31T11:00:00",
      "officer": "Sample Officer",
      "content": "Reviewed allegation summary"
    }
  ]
}
```

- **Response:** (200 OK)

```json
{
  "success": true,
  "message": "Case updated"
}
```

---

### 6. Fetch GitHub Cases

**Retrieve cases from GitHub repository**

- **Method:** GET
- **Endpoint:** `/github/cases`
- **Auth Required:** No
- **Response:** (200 OK)

```json
{
  "success": true,
  "message": "Cases fetched from GitHub",
  "cases": [
    {
      "enquiry_number": "286/2024",
      "accused_names": ["Sample Subject A"],
      "amount_pkr": 2500000,
      "status": "converted_fir"
    }
  ]
}
```

- **Error Response:** (500 Internal Server Error)

```json
{
  "success": false,
  "message": "Failed to fetch from GitHub"
}
```

---

### 7. Get GitHub Repository Info

**Retrieve repository metadata**

- **Method:** GET
- **Endpoint:** `/github/info`
- **Auth Required:** No
- **Response:** (200 OK)

```json
{
  "success": true,
  "repo_name": "aml-case-data",
  "description": "AML Case Data Repository",
  "stars": 15,
  "forks": 3,
  "url": "https://github.com/AML-AMLC/aml-case-data"
}
```

---

### 8. Get Dashboard Analytics

**Retrieve dashboard statistics**

- **Method:** GET
- **Endpoint:** `/analytics/dashboard`
- **Auth Required:** Yes
- **Response:** (200 OK)

```json
{
  "total_cases": 102,
  "active_cases": 42,
  "high_risk": 18,
  "total_amount_involved": 500000000,
  "average_risk_score": 58.5
}
```

---

### 9. Export Cases to CSV

**Export all cases as CSV file**

- **Method:** GET
- **Endpoint:** `/export/cases`
- **Auth Required:** Yes
- **Response:** CSV file download

```
Content-Type: text/csv
Content-Disposition: attachment; filename="cases_export.csv"
```

---

## Error Codes

| Code | Message | Meaning |
|------|---------|---------|
| 200 | OK | Request successful |
| 201 | Created | Resource created successfully |
| 400 | Bad Request | Invalid request parameters |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Access denied |
| 404 | Not Found | Resource not found |
| 500 | Server Error | Internal server error |

---

## Request/Response Examples

### Example 1: Create a case with cURL

```bash
curl -X POST http://localhost:5000/api/cases \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_token_here" \
  -d '{
    "enquiry_number": "123/2024",
    "date_created": "2024-01-31",
    "source": "FMU",
    "category": "STR",
    "accused_names": ["Sample Subject A"],
    "cnic_numbers": ["00000-0000000-0"],
    "allegation_summary": "Suspicious hawala transaction",
    "amount_pkr": 2500000,
    "sensitivity_level": "high"
  }'
```

### Example 2: List cases with filters

```bash
curl -X GET "http://localhost:5000/api/cases?limit=10&offset=0&status=under_probe" \
  -H "Authorization: Bearer your_token_here"
```

### Example 3: Update case status

```bash
curl -X PUT http://localhost:5000/api/cases/550e8400-e29b-41d4-a716-446655440000 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_token_here" \
  -d '{
    "status": "converted_fir",
    "priority": "high"
  }'
```

---

## Status Values

- `pending` - Case newly created, awaiting review
- `under_probe` - Active investigation
- `converted_fir` - Converted to First Information Report
- `transferred` - Transferred to other agency
- `closed` - Investigation closed
- `rejected` - Case rejected

---

## Priority Levels

- `low` - Low priority
- `medium` - Medium priority
- `high` - High priority
- `critical` - Critical/Urgent

---

## Case Categories

- `STR` - Suspicious Transaction Report
- `complaint` - Direct complaint
- `referral` - Referral complaint
- `analysis` - Strategic analysis

---

## Sensitivity Levels

- `normal` - Normal case
- `political` - Political involvement
- `high` - High profile case
- `international` - International implications

---

## Rate Limiting

- API calls are limited to prevent abuse
- Check response headers for rate limit info
- Respect GitHub API limits when syncing

---

## API Versioning

Current API Version: **3.0**

---

## Support

For issues or questions:

- Check logs: `aml_system.log`
- Review README.md
- Contact: AML AMLC Lahore

