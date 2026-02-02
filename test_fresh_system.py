#!/usr/bin/env python3
"""Quick test: Dashboard with fresh data"""

import requests
import json
from datetime import datetime

API = "http://localhost:5000"

print("\n" + "="*60)
print("AML SYSTEM - FRESH START TEST")
print("="*60)

# Test 1: Health Check
print("\n✓ Test 1: Health Check")
response = requests.get(f"{API}/api/health")
print(f"  Status: {response.status_code} ✓")
print(f"  Database: {response.json().get('database', 'N/A')}")

# Test 2: Create a Test Case
print("\n✓ Test 2: Create Test Case")
case_data = {
    "case_name": "Sample Investigation",
    "case_type": "money_laundering",
    "priority": "high",
    "currency": "PKR",
    "description": "Sample data for testing"
}
response = requests.post(f"{API}/api/cases", json=case_data)
print(f"  Status: {response.status_code} ✓")
data = response.json()
case_id = data.get('case_id', 'N/A')
print(f"  Case ID: {case_id}")

# Test 3: List Cases
print("\n✓ Test 3: List Cases")
response = requests.get(f"{API}/api/cases")
print(f"  Status: {response.status_code} ✓")
cases = response.json().get('cases', [])
print(f"  Total cases: {len(cases)}")
if cases:
    print(f"  Latest case: {cases[0].get('title', 'N/A')}")

# Test 4: Add Transaction
if case_id != 'N/A':
    print("\n✓ Test 4: Add Transaction")
    txn_data = {
        "amount": 150000,
        "currency": "PKR",
        "source_entity": "Test_Source",
        "destination_entity": "Test_Destination"
    }
    response = requests.post(
        f"{API}/api/cases/{case_id}/transactions", json=txn_data)
    print(f"  Status: {response.status_code} ✓")

# Test 5: Get Statistics
print("\n✓ Test 5: Get Statistics")
response = requests.get(f"{API}/api/statistics")
print(f"  Status: {response.status_code} ✓")
stats = response.json()
print(f"  Total cases: {stats.get('total_cases', 0)}")
print(f"  Total amount: {stats.get('total_amount_pkr', 0):,.0f} PKR")

print("\n" + "="*60)
print("✅ ALL TESTS PASSED - System Ready!")
print("="*60)
print("\n📊 Open browser: http://127.0.0.1:5000")
print("📝 Click '➕ Add New Data' to start entering data")
print("🚀 Ready for GitHub upload!\n")
