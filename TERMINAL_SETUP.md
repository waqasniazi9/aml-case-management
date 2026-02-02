# Terminal Configuration Guide - AML System v3.5

## ✅ System Status: FULLY OPERATIONAL

All tests are passing. The system is ready to use.

---

## Terminal Setup

### 1. Open PowerShell in the Project Directory

```powershell
cd "c:\Users\OTS\OneDrive\Desktop\Aml_Case_Management_sysyem"
```

### 2. Clear Terminal (Optional)

```powershell
Clear-Host
```

### 3. Start the Server

```powershell
python aml_system.py
```

Expected output:

```
Database initialized successfully with Solana/Token ACL and Cybersecurity Threat tables
Flask application initialized successfully
Starting AML AML Case Management System v3.5
Running on http://127.0.0.1:5000
```

---

## Running Tests

### In-Process Test (No Server Needed)

```powershell
python direct_system_test.py
```

**Expected Output:**

```
======================================================================
DIRECT SYSTEM TEST - Running in-process
======================================================================

[TEST 1] Health Check
✅ Status: 200
   Version: 3.5
   Status: healthy

[TEST 2] Threat Ingestion
✅ Status: 201
   Message: Threat ingested successfully

[TEST 3] Threat Summary
✅ Status: 200
   Total threats: 5
   Total indicators: 7

[TEST 4] Threat Dashboard
✅ Status: 200
   Total threats: 5
   Critical threats: 1

======================================================================
✅ ALL TESTS PASSED - SYSTEM FULLY OPERATIONAL
======================================================================
```

### Integration Test (Requires Running Server)

In a second terminal:

```powershell
python test_rebuilt_system.py
```

---

## Clean Up Previous Processes

If you see connection errors, clean up lingering processes:

```powershell
# Stop all Python processes
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force

# Verify port 5000 is free
netstat -ano | Select-String "5000"

# Should show no output if port is free
```

---

## Quick API Tests

Once server is running, test endpoints in another terminal:

### Test 1: Health Check

```powershell
curl http://127.0.0.1:5000/api/health
```

### Test 2: Threat Summary

```powershell
curl http://127.0.0.1:5000/api/threats/summary
```

### Test 3: Threat Dashboard

```powershell
curl http://127.0.0.1:5000/api/threats/dashboard
```

---

## Terminal Environment Notes

### PowerShell vs CMD

- Use **PowerShell** (recommended) for better output
- CMD works but doesn't display logging as cleanly

### Python Path

- Python should be in your PATH
- If `python` command not found, use full path:

  ```powershell
  C:\Users\OTS\AppData\Local\Python\pythoncore-3.14-64\python.exe aml_system.py
  ```

### Virtual Environment (Optional)

- If you want to use venv (optional):

  ```powershell
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  ```

---

## Troubleshooting

### Issue: "python command not found"

**Solution:**

```powershell
# Check Python installation
python --version

# If not found, use full path
"C:\Users\OTS\AppData\Local\Python\pythoncore-3.14-64\python.exe" aml_system.py
```

### Issue: "Port 5000 already in use"

**Solution:**

```powershell
# Kill existing processes
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force

# Wait 2 seconds
Start-Sleep -Seconds 2

# Try again
python aml_system.py
```

### Issue: "Module not found" or import errors

**Solution:**

```powershell
# Install/update dependencies
pip install flask flask-cors requests pyjwt base58

# Then try running again
python aml_system.py
```

### Issue: Database connection error

**Solution:**

```powershell
# Remove old database to recreate it
Remove-Item -Path aml_system.db -Force -ErrorAction SilentlyContinue

# Server will recreate on startup
python aml_system.py
```

---

## Log Output Explanation

### Normal Startup Log

```
2026-01-31 22:40:13,222 - aml_system - INFO - Database initialized successfully...
2026-01-31 22:40:13,229 - aml_system - INFO - Flask application initialized...
Running on http://127.0.0.1:5000
```

This is **normal** - logging output mixes with Flask output.

### Error Indicators

- `ERROR` in output = Something failed
- `Exception` in output = Code error
- `Connection refused` = Server not running
- Exit code `1` = Failure

### Success Indicators

- `Status: 200` = Endpoint working
- `Status: 201` = Resource created
- `ALL TESTS PASSED` = System good
- Exit code `0` = Success

---

## Common Workflows

### Development Session

```powershell
# Terminal 1: Start server
python aml_system.py

# Terminal 2: Run tests
python direct_system_test.py

# Terminal 3: Test specific endpoints
curl http://127.0.0.1:5000/api/health
```

### Quick Verification

```powershell
# Entire session in one terminal
python direct_system_test.py
# No server needed - tests run in-process
```

### Production-like Testing

```powershell
# Terminal 1: Start server
python aml_system.py

# Terminal 2: Send real request
$data = @{
    title="New Threat"
    category="malware"
    severity="high"
    affected_systems=@("Linux","Windows")
    indicators=@("hash123","domain.com")
    indicator_type="malware_hash"
    source="Research"
    discovered_date="2024-01-31T10:00:00"
    recommendations=@("Patch")
    related_packages=@("pkg1")
    attack_vector="Network"
}

curl -Method Post `
  -Uri http://127.0.0.1:5000/api/threats/ingest `
  -ContentType "application/json" `
  -Body ($data | ConvertTo-Json)
```

---

## Summary

✅ **System Status:** Fully Operational  
✅ **All Tests:** Passing  
✅ **Database:** Initialized with sample data  
✅ **API:** Ready for requests  

**Next Step:** Start the server with `python aml_system.py`

---

*Terminal Configuration Guide - AML System v3.5*  
*Last Updated: January 31, 2026*

