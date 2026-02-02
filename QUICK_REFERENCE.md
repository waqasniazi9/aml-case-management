# 🚀 QUICK REFERENCE - Solana Token ACL Integration

## ⚡ 60-Second Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run system
python aml_system.py

# 3. Test endpoints (in another terminal)
python test_solana_acl.py

# 4. Access web UI
# Open: http://localhost:5000/static/aml3_system.html
```

---

## 📡 API Endpoints Cheat Sheet

### Wallet Management

| Action | Endpoint | Method |
|--------|----------|--------|
| Register wallet | `/api/solana/wallet/register` | POST |
| Get wallet | `/api/solana/wallet/{address}` | GET |
| Check compliance | `/api/solana/wallet/{address}/compliance` | GET |
| Update compliance | `/api/solana/wallet/{address}/compliance` | PUT |

### Token & ACL

| Action | Endpoint | Method |
|--------|----------|--------|
| Add token account | `/api/solana/token-account` | POST |
| Configure ACL | `/api/solana/acl/configure` | POST |
| Record transaction | `/api/solana/acl/transaction` | POST |

### Analysis

| Action | Endpoint | Method |
|--------|----------|--------|
| Analyze transfer | `/api/solana/transfer/analyze` | POST |
| Detect patterns | `/api/solana/patterns/detect/{address}` | GET |
| Dashboard stats | `/api/solana/dashboard` | GET |

---

## 🎯 Common Operations

### Register a Wallet

```bash
curl -X POST http://localhost:5000/api/solana/wallet/register \
  -H "Content-Type: application/json" \
  -d '{
    "address": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
    "owner_name": "Suspect Name",
    "kyc_status": false,
    "is_whitelisted": false,
    "is_blacklisted": false
  }'
```

### Check Compliance

```bash
curl http://localhost:5000/api/solana/wallet/9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q/compliance
```

### Analyze Transfer

```bash
curl -X POST http://localhost:5000/api/solana/transfer/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "from_wallet": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
    "to_wallet": "AnotherAddress...",
    "amount": 50000000,
    "token_mint": "EPjFWaJwqNog3jFfSo0ggUkh2B8ZwQEoR1ZcMV9B534m"
  }'
```

### Get Dashboard

```bash
curl http://localhost:5000/api/solana/dashboard
```

---

## 📊 Compliance Scoring

```
Score Calculation:
┌─ Base: 50
├─ +20: KYC verified
├─ +15: Whitelisted  
├─ -40: Blacklisted
└─ Result: 0-100

Risk Levels:
80-100 → Green (Low Risk)
60-79  → Yellow (Medium Risk)
40-59  → Orange (High Risk)
0-39   → Red (Critical)
```

---

## 🗄️ Database Tables

```
solana_wallets
├── id, address, owner_name
├── kyc_status, aml_case_id
├── is_whitelisted, is_blacklisted
└── created_at, updated_at

token_accounts
├── id, account_address, owner_address
├── is_frozen, acl_status, list_type
├── associated_case_id
└── created_at

token_acl_config
├── id, mint_address, gate_program
├── authority_pubkey, list_type
├── permissionless_freeze, permissionless_thaw
├── associated_case_id
└── created_at

acl_transactions
├── id, transaction_hash, action_type
├── wallet_address, token_account
├── compliance_status, associated_case_id
└── created_at
```

---

## 🧪 Test Commands

```bash
# Run all Solana ACL tests
python test_solana_acl.py

# Run specific test (Python interactive)
python -c "from test_solana_acl import *; test_wallet_registration()"

# Run AML tests
python test_api.py

# View logs
tail -f aml_system.log
```

---

## 📁 Key Files

```
aml_system.py          # Main application (2,273 lines)
test_solana_acl.py     # Solana tests (350+ lines)
SOLANA_ACL_INTEGRATION.md  # Complete API guide
README_v3.5.md         # System documentation
requirements.txt       # Dependencies
```

---

## 🔧 Environment Variables (Optional)

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key
export DATABASE_PATH=/path/to/db.sqlite
export SOLANA_CLUSTER=mainnet-beta
export LOG_LEVEL=INFO
```

---

## ⚠️ Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| Port 5000 in use | `lsof -ti:5000 \| xargs kill -9` |
| Module not found | `pip install -r requirements.txt` |
| Database lock | Restart application |
| Invalid address | Verify Base58 Solana address format |
| Import error | Check Python version (3.8+) |

---

## 📞 Documentation Links

- 📖 **Full README:** [README_v3.5.md](README_v3.5.md)
- 🔌 **API Reference:** [SOLANA_ACL_INTEGRATION.md](SOLANA_ACL_INTEGRATION.md)
- 📋 **Implementation:** [INTEGRATION_SUMMARY.md](INTEGRATION_SUMMARY.md)
- ✅ **Status:** [SOLANA_INTEGRATION_COMPLETE.md](SOLANA_INTEGRATION_COMPLETE.md)

---

## 🎯 Workflow (5 Steps)

```
1. REGISTER
   POST /api/solana/wallet/register
   
2. VERIFY
   PUT /api/solana/wallet/{address}/compliance
   
3. CONFIGURE
   POST /api/solana/acl/configure
   
4. MONITOR
   POST /api/solana/transfer/analyze
   
5. REPORT
   GET /api/solana/dashboard
```

---

## 📊 System Stats

- **Version:** 3.5
- **Endpoints:** 22 total (9 AML + 13 Solana)
- **Database Tables:** 8
- **Test Cases:** 24+
- **Documentation Pages:** 8
- **Code Lines:** 2,273+

---

## ✅ Verification

Run this to verify everything works:

```bash
# Check system health
curl http://localhost:5000/api/health

# Check Solana dashboard
curl http://localhost:5000/api/solana/dashboard

# Run test suite
python test_solana_acl.py
```

---

## 🎉 You're Ready

The Solana Token ACL integration is **complete and operational**.

Next: Start the server and explore the API!

```bash
python aml_system.py
```

Then visit: **<http://localhost:5000>**

---

*For detailed documentation, see SOLANA_ACL_INTEGRATION.md*
