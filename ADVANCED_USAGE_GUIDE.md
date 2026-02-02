# AML SYSTEM v6.0 - ADVANCED USAGE & MIGRATION GUIDE

## Quick Start with Enhanced Features

### Step 1: Setup Environment

```bash
# Create virtual environment
python -m venv venv
./venv/Scripts/activate  # Windows

# Install enhanced requirements
pip install -r requirements.txt

# Run the system
python aml_system_v6_enhanced.py
```

---

## Advanced Features Guide

### 1. ANOMALY DETECTION IN ACTION

#### Creating a Case with Suspicious Transactions

```bash
# Step 1: Create an entity
curl -X POST http://localhost:5000/api/entities \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Ahmed Khan",
    "entity_type": "person",
    "cnic_number": "00000-0000000-0",
    "pep_flag": false,
    "sanctions_flag": false
  }'
# Response: {"entity_id": "abc123"}

# Step 2: Create another entity
curl -X POST http://localhost:5000/api/entities \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Local Business",
    "entity_type": "organization"
  }'
# Response: {"entity_id": "def456"}

# Step 3: Create a case
curl -X POST http://localhost:5000/api/cases \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Structuring Activity Investigation",
    "description": "Multiple small transfers detected",
    "case_type": "structuring",
    "amount_involved": 500000,
    "risk_level": "high",
    "accused_names": "Ahmed Khan"
  }'
# Response: {"case_id": "xyz789"}

# Step 4: Add normal transaction
curl -X POST http://localhost:5000/api/cases/xyz789/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "source_entity": "abc123",
    "destination_entity": "def456",
    "amount": 10000,
    "currency": "PKR",
    "transaction_date": "2024-01-15T10:30:00",
    "transaction_type": "transfer",
    "description": "Regular business transfer"
  }'

# Step 5: Add anomalous transaction (unusual amount)
curl -X POST http://localhost:5000/api/cases/xyz789/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "source_entity": "abc123",
    "destination_entity": "def456",
    "amount": 250000,
    "currency": "PKR",
    "transaction_date": "2024-01-15T11:30:00",
    "transaction_type": "transfer",
    "description": "Unusual large transfer"
  }'

# The system AUTOMATICALLY detects this anomaly with:
# - Z-score: 2.45 (highly unusual amount)
# - Reason: "Unusual transaction amount"
# - Anomaly Score: 24.5/100
```

#### Retrieve Anomaly Analysis

```bash
curl http://localhost:5000/api/cases/xyz789/analysis

# Response includes:
{
  "case_id": "xyz789",
  "patterns": {
    "structuring": {
      "confidence": 0.95,
      "total_amount": 260000,
      "transaction_count": 2
    }
  },
  "risk_assessment": {
    "case_risk_score": 72.5,
    "risk_level": "high"
  },
  "anomalies": [
    {
      "transaction_id": "txn123",
      "score": 24.5,
      "reasons": ["Unusual transaction amount (Z-score: 2.45)"]
    }
  ]
}
```

---

### 2. PATTERN DETECTION - STRUCTURING

#### Detecting Smurfing Activity

```bash
# Scenario: Criminal structures 5M PKR into 10x 500K transfers

# Create source entity
curl -X POST http://localhost:5000/api/entities \
  -H "Content-Type: application/json" \
  -d '{"name": "Smurf Source", "entity_type": "person"}'
# Response: {"entity_id": "smurf1"}

# Create case
curl -X POST http://localhost:5000/api/cases \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Potential Structuring Detected",
    "case_type": "structuring",
    "amount_involved": 5000000,
    "risk_level": "critical"
  }'
# Response: {"case_id": "struct_case"}

# Add 10 identical 500K transfers
for i in {1..10}; do
  curl -X POST http://localhost:5000/api/cases/struct_case/transactions \
    -H "Content-Type: application/json" \
    -d '{
      "source_entity": "smurf1",
      "destination_entity": "dest'$i'",
      "amount": 500000,
      "currency": "PKR",
      "transaction_date": "2024-01-15T'$((10+i))':00:00"
    }'
done

# Analyze - System AUTOMATICALLY detects:
# Pattern: STRUCTURING
# Confidence: 0.95 (95% certain)
# Reason: 10 transactions, each 500K (below 1M threshold)
# Total: 5,000,000 PKR
```

---

### 3. NETWORK ANALYSIS - FAN PATTERNS

#### Detecting Money Collection (Fan-In)

```bash
# Scenario: Many accounts sending to one account (collection point)

# Create 20 source entities
for i in {1..20}; do
  curl -X POST http://localhost:5000/api/entities \
    -H "Content-Type: application/json" \
    -d '{"name": "Source'$i'", "entity_type": "account"}'
done

# Create hub entity (collection point)
curl -X POST http://localhost:5000/api/entities \
  -H "Content-Type: application/json" \
  -d '{"name": "Hub Account", "entity_type": "account"}'
# Response: {"entity_id": "hub1"}

# Create case
curl -X POST http://localhost:5000/api/cases \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Fan-In Activity",
    "case_type": "hawala",
    "amount_involved": 10000000
  }'
# Response: {"case_id": "fanin_case"}

# Add transactions from multiple sources to hub
for i in {1..20}; do
  curl -X POST http://localhost:5000/api/cases/fanin_case/transactions \
    -H "Content-Type: application/json" \
    -d '{
      "source_entity": "source'$i'",
      "destination_entity": "hub1",
      "amount": 500000,
      "currency": "PKR",
      "transaction_date": "2024-01-15T'$((10+i))':00:00",
      "description": "Collection"
    }'
done

# Analyze case
curl http://localhost:5000/api/cases/fanin_case/analysis

# Response detects:
# Network Pattern: FAN_IN
# Count: 20 inbound connections
# Total Amount: 10,000,000 PKR
# Risk Score: 80+ (Critical)
```

#### Detecting Money Distribution (Fan-Out)

```bash
# Similar to fan-in but reverse:
# One account sends to many accounts

# Create hub entity
curl -X POST http://localhost:5000/api/entities \
  -H "Content-Type: application/json" \
  -d '{"name": "Distribution Hub", "entity_type": "account"}'
# Response: {"entity_id": "dist_hub"}

# Create case
curl -X POST http://localhost:5000/api/cases \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Fan-Out Activity",
    "case_type": "smuggling",
    "amount_involved": 15000000
  }'

# Add outbound transactions from hub
for i in {1..15}; do
  curl -X POST http://localhost:5000/api/cases/<case_id>/transactions \
    -H "Content-Type: application/json" \
    -d '{
      "source_entity": "dist_hub",
      "destination_entity": "dest'$i'",
      "amount": 1000000,
      "currency": "PKR"
    }'
done

# Analysis detects:
# Pattern: FAN_OUT
# Outbound Destinations: 15
# Risk: 80+
```

---

### 4. ROUND-TRIPPING DETECTION

#### Detecting Quick Reversal Pattern

```bash
# Scenario: Funds sent out then quickly returned

# Create entities
curl -X POST http://localhost:5000/api/entities \
  -d '{"name": "Trader A", "entity_type": "person"}' \
  -H "Content-Type: application/json"
# Response: {"entity_id": "trader_a"}

curl -X POST http://localhost:5000/api/entities \
  -d '{"name": "Trader B", "entity_type": "person"}' \
  -H "Content-Type: application/json"
# Response: {"entity_id": "trader_b"}

# Create case
curl -X POST http://localhost:5000/api/cases \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Round-Tripping Detection",
    "case_type": "trade_based",
    "amount_involved": 2000000
  }'
# Response: {"case_id": "roundtrip_case"}

# Transaction 1: A → B (1M PKR)
curl -X POST http://localhost:5000/api/cases/roundtrip_case/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "source_entity": "trader_a",
    "destination_entity": "trader_b",
    "amount": 1000000,
    "currency": "PKR",
    "transaction_date": "2024-01-15T10:00:00",
    "description": "Trade payment"
  }'

# Transaction 2: B → A (1.02M PKR, 2 days later - slight amount difference)
curl -X POST http://localhost:5000/api/cases/roundtrip_case/transactions \
  -H "Content-Type: application/json" \
  -d '{
    "source_entity": "trader_b",
    "destination_entity": "trader_a",
    "amount": 1020000,
    "currency": "PKR",
    "transaction_date": "2024-01-17T09:00:00",
    "description": "Return payment"
  }'

# Analyze - System detects:
# Pattern: ROUND_TRIPPING
# Confidence: 0.90
# Days Between: 2
# Amount Variance: 2%
# Risk: 75+ (High)
```

---

### 5. COMPREHENSIVE CASE ANALYSIS

```bash
# Get full analysis of case
curl http://localhost:5000/api/cases/roundtrip_case/analysis

# Response Structure:
{
  "case_id": "roundtrip_case",
  "patterns": {
    "round_tripping": {
      "pattern": "round_tripping",
      "confidence": 0.90,
      "round_trip_count": 1,
      "examples": [
        {
          "counterparty": "trader_b",
          "amount": 1000000,
          "days_between": 2
        }
      ]
    }
  },
  "network_analysis": {
    "total_entities": 2,
    "high_centrality_nodes": {
      "trader_a": 15.5,
      "trader_b": 12.3
    },
    "suspicious_chains": []
  },
  "risk_assessment": {
    "case_risk_score": 75.2,
    "risk_level": "high"
  },
  "anomalies": [
    {
      "transaction_id": "txn456",
      "score": 35.0,
      "reasons": ["New counterparty entity"]
    }
  ]
}
```

---

### 6. STATISTICS & REPORTING

```bash
# Get comprehensive system statistics
curl http://localhost:5000/api/statistics

# Response:
{
  "total_cases": 45,
  "total_amount_pkr": 500000000,
  "high_priority_cases": 3,
  "high_risk_cases": 12,
  "average_network_risk_score": 58.3,
  "by_status": {
    "open": 20,
    "under_investigation": 15,
    "escalated": 5,
    "sar_generated": 3,
    "closed": 2
  },
  "by_type": {
    "structuring": 12,
    "hawala": 8,
    "terrorism": 3,
    "fraud": 15,
    "trade_based": 7
  },
  "by_risk": {
    "low": 10,
    "medium": 20,
    "high": 12,
    "critical": 3
  }
}
```

---

## Performance Tuning

### 1. Database Optimization

```python
# Already enabled in v6.0:
# - WAL Mode (Write-Ahead Logging)
# - Foreign Keys (Referential Integrity)
# - Strategic Indexing

# For production with PostgreSQL:
# 1. Install: pip install psycopg2-binary
# 2. Update connection string in DatabaseManager
# 3. Can handle millions of transactions
```

### 2. Batch Operations

```python
# For bulk transaction ingestion:

transactions_batch = [
  (txn_id1, case_id, source1, dest1, amount1, ...),
  (txn_id2, case_id, source2, dest2, amount2, ...),
  # ... up to 10K transactions
]

db.execute_many("""
  INSERT INTO transactions 
  (transaction_id, case_id, ...) VALUES (?, ?, ...)
""", transactions_batch)

# 10K transactions in <100ms
```

### 3. Caching

```python
# Anomaly scores are cached per entity
@lru_cache(maxsize=10000)
def get_entity_anomaly_baseline(entity_id: str):
    # Returns cached baseline
    return baseline_stats[entity_id]

# Clear cache periodically:
get_entity_anomaly_baseline.cache_clear()
```

---

## Migration from v5.0 to v6.0

### Step 1: Backup Existing Data

```bash
# Backup current database
cp aml_system.db aml_system_v5_backup.db

# Backup configuration
cp aml_system.py aml_system_v5.py
```

### Step 2: Deploy v6.0

```bash
# Update requirements
pip install -r requirements.txt

# The new database schema will auto-create with:
# - Additional tables (entities, patterns, anomaly_scores, etc.)
# - Optimized indexes
# - Enhanced foreign key constraints
```

### Step 3: Data Migration (Optional)

```python
# Script to migrate existing cases to v6.0 format
import sqlite3

old_db = sqlite3.connect('aml_system_v5_backup.db')
new_db = sqlite3.connect('aml_system.db')

# Copy cases
old_cursor = old_db.cursor()
new_cursor = new_db.cursor()

old_cursor.execute("SELECT * FROM aml_cases")
for row in old_cursor.fetchall():
    new_cursor.execute("""
        INSERT INTO aml_cases VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0.0, '', 0, ?, ?, ?)
    """, row)

new_db.commit()
```

---

## Troubleshooting

### Issue: "No module named 'numpy'"

```bash
pip install numpy==1.24.3
```

### Issue: Database locked

```python
# Already handled with WAL mode, but if needed:
# Close all connections and restart
```

### Issue: Slow queries

```bash
# Run analysis on case with 10K+ transactions
# Use PRAGMA analyze to update statistics
db.execute_query("PRAGMA analyze")
```

---

## Next Steps

1. **Test with Sample Data**
   - Run provided example scenarios
   - Validate pattern detection
   - Verify risk scoring

2. **Production Deployment**
   - Switch to PostgreSQL
   - Add Redis caching
   - Deploy with Gunicorn

3. **Integrate External Data**
   - Import sanctions lists
   - Connect PEP databases
   - Setup threat feeds

4. **Advanced Analytics**
   - Add ML models (sklearn)
   - Implement LSTM (Keras)
   - Blockchain integration

---

**Version:** 6.0 Enhanced  
**Last Updated:** February 2026
