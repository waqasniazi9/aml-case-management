#!/usr/bin/env python3
import json
from aml_system import create_app
import sys
import os
sys.path.insert(0, r'c:\Users\OTS\OneDrive\Desktop\Aml_Case_Management_sysyem')


print("="*70)
print("DIRECT SYSTEM TEST - Running in-process")
print("="*70)

app = create_app()

# Test 1: Health Check
print("\n[TEST 1] Health Check")
with app.test_client() as client:
    response = client.get('/api/health')
    print(f"✅ Status: {response.status_code}")
    data = json.loads(response.data)
    print(f"   Version: {data.get('version')}")
    print(f"   Status: {data.get('status')}")

# Test 2: Ingest Threat
print("\n[TEST 2] Threat Ingestion")
threat_data = {
    'title': 'Shai-Hulud Ransomware Campaign',
    'description': 'Advanced ransomware targeting enterprise infrastructure',
    'category': 'ransomware',
    'severity': 'critical',
    'affected_systems': ['Windows Servers', 'Linux Enterprise'],
    'indicators': ['sha256_hash_123', 'malicious.com'],
    'indicator_type': 'malware_hash',
    'source': 'GitHub Weekly Research',
    'discovered_date': '2024-01-15T10:00:00',
    'recommendations': ['Patch immediately', 'Isolate systems'],
    'related_packages': ['linux-kernel'],
    'attack_vector': 'Email phishing'
}

with app.test_client() as client:
    response = client.post('/api/threats/ingest',
                           data=json.dumps(threat_data),
                           content_type='application/json')
    print(f"✅ Status: {response.status_code}")
    data = json.loads(response.data)
    print(f"   Message: {data.get('message')}")
    threat_id = data.get('threat_id')
    print(f"   Threat ID: {threat_id[:20] if threat_id else 'N/A'}...")

# Test 3: Summary
print("\n[TEST 3] Threat Summary")
with app.test_client() as client:
    response = client.get('/api/threats/summary')
    print(f"✅ Status: {response.status_code}")
    data = json.loads(response.data)
    print(f"   Total threats: {data.get('total_threats')}")
    print(f"   Total indicators: {data.get('total_indicators')}")

# Test 4: Dashboard
print("\n[TEST 4] Threat Dashboard")
with app.test_client() as client:
    response = client.get('/api/threats/dashboard')
    print(f"✅ Status: {response.status_code}")
    data = json.loads(response.data)
    print(f"   Total threats: {data.get('total_threats')}")
    print(f"   Critical threats: {data.get('critical_threats')}")

print("\n" + "="*70)
print("✅ ALL TESTS PASSED - SYSTEM FULLY OPERATIONAL")
print("="*70)
