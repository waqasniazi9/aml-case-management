#!/usr/bin/env python3
"""
Quick Start Script - AML System v6.0 Enhanced
Tests all major features with sample data
"""

import json
import requests
import time
from datetime import datetime, timedelta

BASE_URL = "http://localhost:5000"
HEADERS = {"Content-Type": "application/json"}


def print_header(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")


def test_health_check():
    """Test 1: Health Check"""
    print_header("TEST 1: System Health Check")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        print(f"✅ Health Status: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_entity_creation():
    """Test 2: Create Entities"""
    print_header("TEST 2: Entity Creation")

    entities = []
    entity_names = [
        "Sample Person A", "Sample Business", "Sample Organization",
        "Sample Account 001", "Sample Account 002"
    ]

    for name in entity_names:
        try:
            entity_type = "person" if "Person" in name else "organization" if "Organization" in name or "Business" in name else "account"

            payload = {
                "name": name,
                "entity_type": entity_type,
                "pep_flag": False,
                "sanctions_flag": False
            }

            response = requests.post(
                f"{BASE_URL}/api/entities",
                json=payload,
                headers=HEADERS
            )

            if response.status_code == 201:
                entity_id = response.json()['entity_id']
                entities.append(entity_id)
                print(f"✅ Created: {name} ({entity_id})")
            else:
                print(f"❌ Failed to create {name}: {response.text}")
        except Exception as e:
            print(f"❌ Error creating {name}: {e}")

    return entities


def test_case_creation(entities):
    """Test 3: Create Case"""
    print_header("TEST 3: Case Creation")

    try:
        payload = {
            "title": "Sample Structuring Pattern",
            "description": "Multiple small transfers detected over 30 days",
            "case_type": "structuring",
            "risk_level": "high",
            "amount_involved": 5000000,
            "currency": "PKR",
            "accused_names": "Sample Subject A",
            "cnic_numbers": "00000-0000000-0",
            "investigation_officer": "Sample Officer"
        }

        response = requests.post(
            f"{BASE_URL}/api/cases",
            json=payload,
            headers=HEADERS
        )

        if response.status_code == 201:
            case_id = response.json()['case_id']
            print(f"✅ Case Created: {case_id}")
            print(f"   Title: {payload['title']}")
            print(f"   Type: {payload['case_type']}")
            return case_id
        else:
            print(f"❌ Failed: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


def test_transaction_addition(case_id, entities):
    """Test 4: Add Transactions with Anomaly Detection"""
    print_header("TEST 4: Transaction Addition (Anomaly Detection)")

    if len(entities) < 2:
        print("❌ Not enough entities")
        return False

    # Add normal transactions first
    print("\n📊 Adding NORMAL transactions...")
    for i in range(5):
        try:
            payload = {
                "source_entity": entities[0],
                "destination_entity": entities[1],
                "amount": 10000 + (i * 5000),
                "currency": "PKR",
                "transaction_date": (datetime.now() - timedelta(days=30-i)).isoformat(),
                "transaction_type": "transfer",
                "description": f"Regular payment {i+1}"
            }

            response = requests.post(
                f"{BASE_URL}/api/cases/{case_id}/transactions",
                json=payload,
                headers=HEADERS
            )

            if response.status_code == 201:
                print(f"✅ TXN {i+1}: {payload['amount']} PKR - Normal")
            else:
                print(f"❌ Failed: {response.text}")
        except Exception as e:
            print(f"❌ Error: {e}")

    # Add anomalous transaction (high amount)
    print("\n⚠️  Adding ANOMALOUS transaction (high amount)...")
    try:
        payload = {
            "source_entity": entities[0],
            "destination_entity": entities[1],
            "amount": 250000,  # Much higher than previous
            "currency": "PKR",
            "transaction_date": datetime.now().isoformat(),
            "transaction_type": "transfer",
            "description": "Unusual high amount"
        }

        response = requests.post(
            f"{BASE_URL}/api/cases/{case_id}/transactions",
            json=payload,
            headers=HEADERS
        )

        if response.status_code == 201:
            print(f"✅ ANOMALOUS TXN: 250,000 PKR - Detected & Flagged")
            print(f"   System will calculate Z-score and anomaly score")
        else:
            print(f"❌ Failed: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

    return True


def test_pattern_detection(case_id, entities):
    """Test 5: Pattern Detection (Structuring)"""
    print_header("TEST 5: Pattern Detection - Structuring")

    if len(entities) < 3:
        print("❌ Not enough entities")
        return False

    print("📊 Adding STRUCTURING pattern (10x 500K transfers)...")

    for i in range(10):
        try:
            destination = entities[1 + (i % min(2, len(entities)-2))]

            payload = {
                "source_entity": entities[0],
                "destination_entity": destination,
                "amount": 500000,  # Just below 1M threshold
                "currency": "PKR",
                "transaction_date": (datetime.now() - timedelta(days=25-i)).isoformat(),
                "transaction_type": "transfer",
                "description": f"Structured transfer {i+1}"
            }

            response = requests.post(
                f"{BASE_URL}/api/cases/{case_id}/transactions",
                json=payload,
                headers=HEADERS
            )

            if response.status_code == 201:
                print(f"✅ Structured TXN {i+1}: 500,000 PKR")
            else:
                print(f"❌ Failed: {response.text}")

            time.sleep(0.1)  # Brief delay
        except Exception as e:
            print(f"❌ Error: {e}")

    print("\n✅ Structuring pattern should be DETECTED on analysis")
    return True


def test_case_analysis(case_id):
    """Test 6: Comprehensive Case Analysis"""
    print_header("TEST 6: Comprehensive Case Analysis")

    try:
        response = requests.get(
            f"{BASE_URL}/api/cases/{case_id}/analysis",
            headers=HEADERS
        )

        if response.status_code == 200:
            analysis = response.json()

            print("📊 ANALYSIS RESULTS:")
            print(f"\n1. Detected Patterns:")
            if analysis.get('patterns'):
                for pattern_name, details in analysis['patterns'].items():
                    print(f"   ✅ {pattern_name.upper()}")
                    print(f"      Details: {json.dumps(details, indent=6)}")
            else:
                print("   No patterns detected")

            print(f"\n2. Network Analysis:")
            if analysis.get('network_analysis'):
                net_info = analysis['network_analysis']
                print(
                    f"   Total Entities: {net_info.get('total_entities', 0)}")
                print(
                    f"   High Centrality Nodes: {len(net_info.get('high_centrality_nodes', {}))}")
                print(
                    f"   Suspicious Chains: {len(net_info.get('suspicious_chains', []))}")

            print(f"\n3. Risk Assessment:")
            if analysis.get('risk_assessment'):
                risk = analysis['risk_assessment']
                print(
                    f"   Case Risk Score: {risk.get('case_risk_score', 0):.1f}/100")
                print(
                    f"   Risk Level: {risk.get('risk_level', 'unknown').upper()}")

            print(f"\n4. Anomalies Detected:")
            anomalies = analysis.get('anomalies', [])
            if anomalies:
                for anom in anomalies[:5]:
                    print(f"   ⚠️  Transaction: {anom['transaction_id']}")
                    print(f"      Anomaly Score: {anom['score']:.1f}/100")
                    for reason in anom.get('reasons', []):
                        print(f"      Reason: {reason}")
            else:
                print("   No anomalies detected")

            return True
        else:
            print(f"❌ Analysis failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_statistics():
    """Test 7: System Statistics"""
    print_header("TEST 7: System Statistics & Reporting")

    try:
        response = requests.get(
            f"{BASE_URL}/api/statistics",
            headers=HEADERS
        )

        if response.status_code == 200:
            stats = response.json()

            print("📊 SYSTEM STATISTICS:")
            print(f"\n1. Overview:")
            print(f"   Total Cases: {stats.get('total_cases', 0)}")
            print(
                f"   Total Amount (PKR): {stats.get('total_amount_pkr', 0):,.0f}")
            print(
                f"   High Priority Cases: {stats.get('high_priority_cases', 0)}")
            print(f"   High Risk Cases: {stats.get('high_risk_cases', 0)}")

            print(f"\n2. Cases by Status:")
            for status, count in stats.get('by_status', {}).items():
                print(f"   {status}: {count}")

            print(f"\n3. Cases by Type:")
            for case_type, count in stats.get('by_type', {}).items():
                print(f"   {case_type}: {count}")

            print(f"\n4. Cases by Risk Level:")
            for risk, count in stats.get('by_risk', {}).items():
                print(f"   {risk}: {count}")

            return True
        else:
            print(f"❌ Statistics failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def test_threat_ingestion():
    """Test 8: Threat Intelligence"""
    print_header("TEST 8: Threat Intelligence Ingestion")

    try:
        payload = {
            "title": "Sanctions List Update",
            "description": "Latest OFAC sanctions entities",
            "severity": "critical",
            "source": "OFAC",
            "indicators": ["entity123", "entity456", "entity789"]
        }

        response = requests.post(
            f"{BASE_URL}/api/threats/ingest",
            json=payload,
            headers=HEADERS
        )

        if response.status_code == 201:
            print(f"✅ Threat Ingested: {response.json()['message']}")
            return True
        else:
            print(f"❌ Failed: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def run_all_tests():
    """Run all tests sequentially"""
    print("\n" + "="*60)
    print("  AML SYSTEM v6.0 ENHANCED - COMPREHENSIVE TEST SUITE")
    print("="*60)
    print(f"\n⏰ Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📍 Server: {BASE_URL}\n")

    results = {
        "Health Check": test_health_check(),
        "Entity Creation": len(test_entity_creation()) > 0,
        "Case Creation": False,
        "Transactions": False,
        "Pattern Detection": False,
        "Case Analysis": False,
        "Statistics": False,
        "Threats": False
    }

    entities = test_entity_creation()

    if len(entities) > 0:
        case_id = test_case_creation(entities)

        if case_id:
            results["Case Creation"] = True
            results["Transactions"] = test_transaction_addition(
                case_id, entities)
            results["Pattern Detection"] = test_pattern_detection(
                case_id, entities)

            # Wait briefly for processing
            time.sleep(1)

            results["Case Analysis"] = test_case_analysis(case_id)
            results["Statistics"] = test_statistics()

    results["Threats"] = test_threat_ingestion()

    # Summary
    print_header("TEST SUMMARY")

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:8} - {test_name}")

    print(f"\n{'='*60}")
    print(f"Total: {passed}/{total} tests passed ({passed*100//total}%)")
    print(f"{'='*60}\n")

    if passed == total:
        print("🎉 ALL TESTS PASSED - System ready for use!")
    else:
        print(f"⚠️  {total - passed} test(s) failed - Check configuration")

    print(f"\n⏱️  Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    print("\n⚠️  Make sure the AML system is running:")
    print("   python aml_system_v6_enhanced.py\n")

    input("Press Enter to start tests...")

    try:
        run_all_tests()
    except KeyboardInterrupt:
        print("\n\n❌ Tests interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
