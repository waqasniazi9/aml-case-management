#!/usr/bin/env python3
"""Quick verification tests for AML System v6.0 Enhanced"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:5000"


def test_health():
    """Test system health"""
    print("\n✓ Testing Health Endpoint...")
    response = requests.get(f"{BASE_URL}/api/health")
    print(f"  Status: {response.status_code}")
    data = response.json()
    print(f"  Database: {data.get('database')}")
    print(f"  Status: {data.get('status')}")
    return response.status_code == 200


def test_entity_creation():
    """Test entity creation"""
    print("\n✓ Testing Entity Creation...")
    entity_data = {
        "entity_id": f"test_entity_{int(time.time())}",
        "entity_type": "individual",
        "name": "Test Entity",
        "risk_level": "medium",
        "metadata": {"test": True}
    }
    response = requests.post(f"{BASE_URL}/api/entities", json=entity_data)
    print(f"  Status: {response.status_code}")
    print(f"  Response: {response.text[:100]}")
    return response.status_code == 201


def test_case_creation():
    """Test case creation"""
    print("\n✓ Testing Case Creation...")
    case_data = {
        "case_id": f"TEST_{int(time.time())}",
        "case_name": "Test Case",
        "case_type": "ongoing_monitoring",
        "priority": "high",
        "description": "Quick test case"
    }
    response = requests.post(f"{BASE_URL}/api/cases", json=case_data)
    print(f"  Status: {response.status_code}")
    print(f"  Response: {response.text[:100]}")
    return response.status_code == 201


def test_list_cases():
    """Test listing cases"""
    print("\n✓ Testing List Cases...")
    response = requests.get(f"{BASE_URL}/api/cases")
    print(f"  Status: {response.status_code}")
    data = response.json()
    print(f"  Cases found: {len(data.get('cases', []))}")
    print(f"  Total: {data.get('total', 0)}")
    return response.status_code == 200


def test_statistics():
    """Test statistics"""
    print("\n✓ Testing Statistics...")
    response = requests.get(f"{BASE_URL}/api/statistics")
    print(f"  Status: {response.status_code}")
    data = response.json()
    for key, value in data.items():
        print(f"  {key}: {value}")
    return response.status_code == 200


def main():
    """Run all tests"""
    print("=" * 60)
    print("AML System v6.0 Enhanced - Quick Verification Tests")
    print("=" * 60)
    print(f"Testing at: {BASE_URL}")
    print(f"Started at: {datetime.now().isoformat()}")

    tests = [
        test_health,
        test_entity_creation,
        test_case_creation,
        test_list_cases,
        test_statistics
    ]

    passed = 0
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"  ERROR: {e}")

    print("\n" + "=" * 60)
    print(f"RESULTS: {passed}/{len(tests)} tests passed")
    print("=" * 60)

    if passed == len(tests):
        print("✓ ALL TESTS PASSED - System is operational!")
    else:
        print(f"⚠ {len(tests) - passed} test(s) failed")


if __name__ == "__main__":
    main()
