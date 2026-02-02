"""
Test suite for Solana Token ACL integration
Tests all ACL endpoints and compliance engine
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:5000/api"

# ANSI color codes for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'


def test_header(test_name):
    print(f"\n{YELLOW}{'='*60}")
    print(f"Testing: {test_name}")
    print(f"{'='*60}{RESET}")


def test_success(message):
    print(f"{GREEN}✓ {message}{RESET}")


def test_error(message):
    print(f"{RED}✗ {message}{RESET}")


def test_info(message):
    print(f"{YELLOW}ℹ {message}{RESET}")

# ==================== WALLET TESTS ====================


def test_wallet_registration():
    """Test wallet registration"""
    test_header("Wallet Registration")

    wallet_data = {
        "address": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
        "owner_name": "Test Wallet Owner",
        "kyc_status": True,
        "is_whitelisted": True,
        "is_blacklisted": False
    }

    try:
        response = requests.post(
            f"{BASE_URL}/solana/wallet/register", json=wallet_data)

        if response.status_code == 201:
            data = response.json()
            if data['success']:
                test_success(f"Wallet registered: {data['wallet_id']}")
                return data['wallet_id']
            else:
                test_error(f"Registration failed: {data['message']}")
        else:
            test_error(f"HTTP {response.status_code}: {response.text}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")

    return None


def test_get_wallet_summary(wallet_address):
    """Test fetching wallet summary"""
    test_header("Get Wallet Summary")

    try:
        response = requests.get(f"{BASE_URL}/solana/wallet/{wallet_address}")

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                wallet = data['wallet']
                test_success(f"Wallet found: {wallet['owner_name']}")
                test_info(f"  Address: {wallet['address']}")
                test_info(f"  KYC Status: {wallet['kyc_status']}")
                test_info(f"  Compliance Score: {wallet['compliance_score']}")
                return wallet
            else:
                test_error(f"Fetch failed: {data['message']}")
        else:
            test_error(f"HTTP {response.status_code}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")

    return None


def test_check_compliance(wallet_address):
    """Test compliance check"""
    test_header("Check Wallet Compliance")

    try:
        response = requests.get(
            f"{BASE_URL}/solana/wallet/{wallet_address}/compliance")

        if response.status_code == 200:
            data = response.json()
            compliance = data['compliance']

            if compliance['compliant']:
                test_success(f"Wallet is compliant")
                test_info(f"  Reason: {compliance['reason']}")
                test_info(
                    f"  Whitelisted: {compliance.get('whitelisted', False)}")
                test_info(
                    f"  KYC Verified: {compliance.get('kyc_verified', False)}")
            else:
                test_error(f"Wallet non-compliant: {compliance['reason']}")

            return compliance
        else:
            test_error(f"HTTP {response.status_code}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")

    return None


def test_update_compliance(wallet_address):
    """Test updating wallet compliance"""
    test_header("Update Wallet Compliance")

    compliance_data = {
        "is_whitelisted": False,
        "is_blacklisted": True,
        "kyc_status": False
    }

    try:
        response = requests.put(
            f"{BASE_URL}/solana/wallet/{wallet_address}/compliance",
            json=compliance_data
        )

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                test_success(f"Compliance updated successfully")
            else:
                test_error(f"Update failed: {data['message']}")
        else:
            test_error(f"HTTP {response.status_code}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")

# ==================== TOKEN ACCOUNT TESTS ====================


def test_add_token_account():
    """Test adding token account"""
    test_header("Add Token Account")

    account_data = {
        "account_address": "ATokenGPvbdGVqstok2z6cBvAm8fWzD21qQvEYh7PzAr",
        "owner_address": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
        "is_frozen": False,
        "acl_status": "COMPLIANT",
        "list_type": "WHITELIST"
    }

    try:
        response = requests.post(
            f"{BASE_URL}/solana/token-account", json=account_data)

        if response.status_code == 201:
            data = response.json()
            if data['success']:
                test_success(
                    f"Token account registered: {account_data['account_address']}")
            else:
                test_error(f"Registration failed: {data['message']}")
        else:
            test_error(f"HTTP {response.status_code}: {response.text}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")

# ==================== ACL CONFIGURATION TESTS ====================


def test_configure_acl():
    """Test ACL configuration"""
    test_header("Configure Token ACL")

    config_data = {
        "mint_address": "EPjFWaJwqNog3jFfSo0ggUkh2B8ZwQEoR1ZcMV9B534m",
        "gate_program": "GateProgramAddressExample123456789",
        "authority_pubkey": "AuthorityPubKeyExample123456789",
        "list_type": "WHITELIST",
        "permissionless_freeze": False,
        "permissionless_thaw": False
    }

    try:
        response = requests.post(
            f"{BASE_URL}/solana/acl/configure", json=config_data)

        if response.status_code == 201:
            data = response.json()
            if data['success']:
                test_success(
                    f"ACL configured for mint: {config_data['mint_address']}")
            else:
                test_error(f"Configuration failed: {data['message']}")
        else:
            test_error(f"HTTP {response.status_code}: {response.text}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")

# ==================== TRANSACTION TESTS ====================


def test_record_transaction():
    """Test recording ACL transaction"""
    test_header("Record ACL Transaction")

    transaction_data = {
        "transaction_hash": "5vWEYLnTa3gN8qE7hFkC8mP9vQ3rS5tU8vW9xY0zZ1aB2cD3eF4gH5iJ6kL",
        "action_type": "FREEZE",
        "wallet_address": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
        "token_account": "ATokenGPvbdGVqstok2z6cBvAm8fWzD21qQvEYh7PzAr",
        "compliance_status": "COMPLIANT"
    }

    try:
        response = requests.post(
            f"{BASE_URL}/solana/acl/transaction", json=transaction_data)

        if response.status_code == 201:
            data = response.json()
            if data['success']:
                test_success(
                    f"Transaction recorded: {transaction_data['transaction_hash'][:20]}...")
            else:
                test_error(f"Recording failed: {data['message']}")
        else:
            test_error(f"HTTP {response.status_code}: {response.text}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")

# ==================== COMPLIANCE ANALYSIS TESTS ====================


def test_analyze_transfer():
    """Test token transfer compliance analysis"""
    test_header("Analyze Token Transfer")

    transfer_data = {
        "from_wallet": "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q",
        "to_wallet": "AnotherWalletAddress9B5X1CbNQ6LHCPqU2UvV5UqKjL4",
        "amount": 1000000,
        "token_mint": "EPjFWaJwqNog3jFfSo0ggUkh2B8ZwQEoR1ZcMV9B534m"
    }

    try:
        response = requests.post(
            f"{BASE_URL}/solana/transfer/analyze", json=transfer_data)

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                analysis = data['analysis']
                if analysis['compliant']:
                    test_success(f"Transfer is COMPLIANT")
                else:
                    test_info(f"Transfer has violations:")
                    for violation in analysis['violations']:
                        test_error(f"  - {violation}")
                    for recommendation in analysis['recommendations']:
                        test_info(f"  → {recommendation}")
            else:
                test_error(f"Analysis failed: {data['message']}")
        else:
            test_error(f"HTTP {response.status_code}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")


def test_detect_patterns():
    """Test suspicious pattern detection"""
    test_header("Detect Suspicious Patterns")

    wallet_address = "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q"

    try:
        response = requests.get(
            f"{BASE_URL}/solana/patterns/detect/{wallet_address}",
            params={"hours": 24}
        )

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                patterns = data['patterns']
                if patterns['suspicious']:
                    test_error(f"SUSPICIOUS ACTIVITY DETECTED")
                    for flag in patterns['flags']:
                        test_error(f"  🚩 {flag}")
                else:
                    test_success(f"No suspicious patterns detected")
                    if patterns['flags']:
                        test_info(f"Alerts:")
                        for flag in patterns['flags']:
                            test_info(f"  ℹ {flag}")
            else:
                test_error(f"Detection failed: {data['message']}")
        else:
            test_error(f"HTTP {response.status_code}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")

# ==================== DASHBOARD TESTS ====================


def test_solana_dashboard():
    """Test Solana dashboard"""
    test_header("Solana Token ACL Dashboard")

    try:
        response = requests.get(f"{BASE_URL}/solana/dashboard")

        if response.status_code == 200:
            data = response.json()
            if data['success']:
                stats = data['dashboard']
                test_success(f"Dashboard retrieved successfully")
                test_info(
                    f"  Registered Wallets: {stats['registered_wallets']}")
                test_info(f"  Compliant Wallets: {stats['compliant_wallets']}")
                test_info(f"  Flagged Wallets: {stats['flagged_wallets']}")
                test_info(
                    f"  Recent Transactions: {stats['recent_transactions']}")
                test_info(f"  Whitelist Tokens: {stats['whitelist_tokens']}")
                test_info(f"  Blacklist Tokens: {stats['blacklist_tokens']}")
            else:
                test_error(f"Dashboard retrieval failed")
        else:
            test_error(f"HTTP {response.status_code}")
    except Exception as e:
        test_error(f"Exception: {str(e)}")

# ==================== MAIN TEST RUNNER ====================


def run_all_tests():
    """Run complete test suite"""
    print(f"\n{YELLOW}{'='*60}")
    print("SOLANA TOKEN ACL INTEGRATION TEST SUITE")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}{RESET}")

    # Register wallet and get ID for other tests
    wallet_id = test_wallet_registration()

    if not wallet_id:
        test_error("Failed to register wallet. Aborting tests.")
        return

    # Wallet tests
    wallet_address = "9B5X1CbNQ6LHCPqU2UvV5UqKjL4aqLhz7mNv1z5K2c3Q"
    test_get_wallet_summary(wallet_address)
    test_check_compliance(wallet_address)

    # Token account tests
    test_add_token_account()

    # ACL configuration tests
    test_configure_acl()

    # Transaction tests
    test_record_transaction()

    # Compliance analysis tests
    test_analyze_transfer()
    test_detect_patterns()

    # Dashboard tests
    test_solana_dashboard()

    print(f"\n{YELLOW}{'='*60}")
    print(
        f"Test suite completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}{RESET}\n")


if __name__ == "__main__":
    print("\nEnsure the AML system is running on http://localhost:5000")
    print("Starting tests in 2 seconds...\n")
    time.sleep(2)

    try:
        run_all_tests()
    except KeyboardInterrupt:
        print(f"\n{RED}Tests interrupted by user{RESET}\n")
    except Exception as e:
        print(f"\n{RED}Unexpected error: {str(e)}{RESET}\n")
