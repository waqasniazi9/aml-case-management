"""
Test suite for Cybersecurity Threat Intelligence Integration
Tests all threat management endpoints
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:5000/api"

# ANSI colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def test_header(name):
    print(f"\n{YELLOW}{'='*60}")
    print(f"Testing: {name}")
    print(f"{'='*60}{RESET}")


def success(msg):
    print(f"{GREEN}✓ {msg}{RESET}")


def error(msg):
    print(f"{RED}✗ {msg}{RESET}")


def info(msg):
    print(f"{BLUE}ℹ {msg}{RESET}")

# ==================== THREAT INGESTION TESTS ====================


def test_ingest_supply_chain_threat():
    """Test ingesting a supply chain threat"""
    test_header("Ingest Supply Chain Threat")

    threat_data = {
        "title": "Shai-Hulud Worm Returns (v2)",
        "description": "Self-replicating npm worm affecting 800+ packages and 27,000+ GitHub repositories",
        "category": "supply_chain",
        "severity": "critical",
        "affected_systems": ["npm", "Maven", "GitHub"],
        "indicators": ["bcryptjs-node", "cross-sessions", "json-oauth", "node-tailwind"],
        "indicator_type": "package_name",
        "source": "Weekly Research",
        "discovered_date": "2025-12-02",
        "recommendations": [
            "Audit npm dependencies immediately",
            "Check for compromised packages",
            "Verify API keys and cloud credentials"
        ],
        "related_packages": ["npm ecosystem", "Maven ecosystem"],
        "attack_vector": "Preinstall scripts for credential theft"
    }

    try:
        response = requests.post(
            f"{BASE_URL}/threats/ingest", json=threat_data)

        if response.status_code == 201:
            data = response.json()
            if data['success']:
                success(f"Supply chain threat ingested: {data['threat_id']}")
                info(f"Title: {threat_data['title']}")
                return data['threat_id']
        else:
            error(f"HTTP {response.status_code}: {response.text}")
    except Exception as e:
        error(f"Exception: {str(e)}")

    return None


def test_ingest_malware_threat():
    """Test ingesting a malware threat"""
    test_header("Ingest Malware Threat")

    threat_data = {
        "title": "OtterCookie Malware - NK Campaign",
        "description": "197 malicious npm packages deployed by NK threat actors (Contagious Interview campaign)",
        "category": "malware",
        "severity": "critical",
        "affected_systems": ["npm packages", "Node.js applications"],
        "indicators": ["bcryptjs-node", "cross-sessions", "json-oauth"],
        "indicator_type": "package_name",
        "source": "Weekly Research",
        "discovered_date": "2025-12-02",
        "recommendations": [
            "Block North Korean threat actor IPs",
            "Scan for OtterCookie indicators",
            "Check wallet data exfiltration"
        ],
        "related_packages": ["npm malicious packages"],
        "attack_vector": "Remote shell, keylogging, screenshot capability"
    }

    try:
        response = requests.post(
            f"{BASE_URL}/threats/ingest", json=threat_data)

        if response.status_code == 201:
            data = response.json()
            if data['success']:
                success(f"Malware threat ingested: {data['threat_id']}")
                info(f"Downloads: 31,000+")
                return data['threat_id']
        else:
            error(f"HTTP {response.status_code}")
    except Exception as e:
        error(f"Exception: {str(e)}")

    return None


def test_ingest_apt_threat():
    """Test ingesting APT threat"""
    test_header("Ingest APT Threat")

    threat_data = {
        "title": "Tomiris APT Campaign",
        "description": "Targets: Foreign ministries, intergovernmental organizations, government entities",
        "category": "apt",
        "severity": "high",
        "affected_systems": ["Russian government entities", "Kyrgyzstan", "Tajikistan", "Uzbekistan"],
        "indicators": ["tomiris-c2", "telegram-c2", "discord-c2"],
        "indicator_type": "ioc",
        "source": "Weekly Research",
        "discovered_date": "2025-12-02",
        "recommendations": [
            "Monitor for APT campaigns",
            "Block Telegram/Discord C2 communications",
            "Implement zero-trust policies"
        ],
        "attack_vector": "Public services (Telegram, Discord) as C2 servers"
    }

    try:
        response = requests.post(
            f"{BASE_URL}/threats/ingest", json=threat_data)

        if response.status_code == 201:
            data = response.json()
            if data['success']:
                success(f"APT threat ingested: {data['threat_id']}")
                return data['threat_id']
        else:
            error(f"HTTP {response.status_code}")
    except Exception as e:
        error(f"Exception: {str(e)}")

    return None

# ==================== THREAT SEARCH TESTS ====================


def test_search_threats_by_title():
    """Test searching threats by title"""
    test_header("Search Threats by Title")

    try:
        response = requests.get(f"{BASE_URL}/threats/search", params={
            'q': 'worm',
            'type': 'title'
        })

        if response.status_code == 200:
            data = response.json()
            success(f"Found {data['count']} threats matching 'worm'")
            for result in data['results']:
                info(f"  - {result['title']} ({result['severity']})")
        else:
            error(f"HTTP {response.status_code}")
    except Exception as e:
        error(f"Exception: {str(e)}")


def test_search_threats_by_category():
    """Test searching threats by category"""
    test_header("Search Threats by Category")

    try:
        response = requests.get(f"{BASE_URL}/threats/search", params={
            'q': 'supply_chain',
            'type': 'category'
        })

        if response.status_code == 200:
            data = response.json()
            success(f"Found {data['count']} supply chain threats")
        else:
            error(f"HTTP {response.status_code}")
    except Exception as e:
        error(f"Exception: {str(e)}")

# ==================== THREAT DETAILS TESTS ====================


def test_get_threat_details(threat_id):
    """Test retrieving threat details"""
    test_header("Get Threat Details")

    try:
        response = requests.get(f"{BASE_URL}/threats/{threat_id}")

        if response.status_code == 200:
            data = response.json()
            threat = data['threat']
            success(f"Retrieved threat: {threat['title']}")
            info(f"  Category: {threat['category']}")
            info(f"  Severity: {threat['severity']}")
            info(
                f"  Affected Systems: {', '.join(threat['affected_systems'])}")
            return threat
        else:
            error(f"HTTP {response.status_code}")
    except Exception as e:
        error(f"Exception: {str(e)}")

    return None

# ==================== THREAT-CASE LINKING TESTS ====================


def test_link_threat_to_case(threat_id):
    """Test linking threat to AML case"""
    test_header("Link Threat to Case")

    # Use a dummy case ID for testing
    case_id = "test-case-123"

    try:
        response = requests.post(f"{BASE_URL}/threats/{threat_id}/link", json={
            "case_id": case_id,
            "association_type": "related"
        })

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                success(f"Threat linked to case {case_id}")
                return True
        else:
            error(f"HTTP {response.status_code}")
    except Exception as e:
        error(f"Exception: {str(e)}")

    return False

# ==================== THREAT SUMMARY TESTS ====================


def test_threats_summary():
    """Test threat summary statistics"""
    test_header("Threats Summary")

    try:
        response = requests.get(f"{BASE_URL}/threats/summary")

        if response.status_code == 200:
            data = response.json()
            summary = data['summary']
            success(f"Threat summary retrieved")
            info(f"  Total Threats: {summary.get('total_threats', 0)}")
            info(f"  Total Indicators: {summary.get('total_indicators', 0)}")

            severity = summary.get('threats_by_severity', {})
            info(
                f"  Critical: {severity.get('critical', 0)}, High: {severity.get('high', 0)}")

            categories = summary.get('threats_by_category', {})
            for cat, count in list(categories.items())[:3]:
                info(f"  {cat}: {count}")
        else:
            error(f"HTTP {response.status_code}")
    except Exception as e:
        error(f"Exception: {str(e)}")


def test_threats_dashboard():
    """Test threat dashboard"""
    test_header("Threats Dashboard")

    try:
        response = requests.get(f"{BASE_URL}/threats/dashboard")

        if response.status_code == 200:
            data = response.json()
            dashboard = data['dashboard']
            success(f"Dashboard retrieved")
            info(f"  Total Threats: {dashboard['total_threats']}")
            info(f"  Critical: {dashboard['critical_threats']}")
            info(f"  High: {dashboard['high_threats']}")
            info(f"  Indicators: {dashboard['total_indicators']}")
            info(
                f"  High Confidence: {dashboard['high_confidence_indicators']}")
        else:
            error(f"HTTP {response.status_code}")
    except Exception as e:
        error(f"Exception: {str(e)}")

# ==================== INDICATOR CHECKING TESTS ====================


def test_check_indicators():
    """Test checking case wallets against threat indicators"""
    test_header("Check Indicators Against Case")

    try:
        response = requests.post(f"{BASE_URL}/threats/indicators/check", json={
            "case_id": "test-case-123"
        })

        if response.status_code == 200:
            data = response.json()
            matches = data['matches']
            success(f"Indicator check completed")
            info(f"  Total Wallets: {matches['total_wallets']}")
            info(f"  Threats Detected: {len(matches['threats_detected'])}")
            info(f"  High Risk Count: {matches['high_risk_count']}")
        else:
            error(f"HTTP {response.status_code}")
    except Exception as e:
        error(f"Exception: {str(e)}")

# ==================== MAIN TEST RUNNER ====================


def run_all_tests():
    """Run complete threat intelligence test suite"""
    print(f"\n{YELLOW}{'='*60}")
    print("CYBERSECURITY THREAT INTELLIGENCE TEST SUITE")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}{RESET}")

    # Ingest threats
    threat_id1 = test_ingest_supply_chain_threat()
    threat_id2 = test_ingest_malware_threat()
    threat_id3 = test_ingest_apt_threat()

    if not threat_id1:
        error("Failed to ingest initial threat. Aborting tests.")
        return

    # Search tests
    test_search_threats_by_title()
    test_search_threats_by_category()

    # Details test
    test_get_threat_details(threat_id1)

    # Linking test
    test_link_threat_to_case(threat_id1)

    # Summary tests
    test_threats_summary()
    test_threats_dashboard()

    # Indicator check
    test_check_indicators()

    print(f"\n{YELLOW}{'='*60}")
    print(
        f"Test suite completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}{RESET}\n")


if __name__ == "__main__":
    print("\nEnsure the AML system is running on http://localhost:5000")
    print("Starting tests in 2 seconds...\n")

    import time
    time.sleep(2)

    try:
        run_all_tests()
    except KeyboardInterrupt:
        print(f"\n{RED}Tests interrupted by user{RESET}\n")
    except Exception as e:
        print(f"\n{RED}Unexpected error: {str(e)}{RESET}\n")
