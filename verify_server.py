#!/usr/bin/env python3
"""Verify AML system server is running and responsive"""

import requests
import time
import sys


def test_connection():
    """Test if server is responding"""
    urls = [
        "http://127.0.0.1:5000/api/threats/dashboard",
        "http://localhost:5000/api/threats/dashboard",
        "http://192.168.100.16:5000/api/threats/dashboard"
    ]

    for url in urls:
        try:
            print(f"Testing: {url}")
            response = requests.get(url, timeout=2)
            print(f"✓ Connected! Status: {response.status_code}")
            print(f"Response: {response.json()}")
            return True
        except Exception as e:
            print(f"✗ Failed: {e}")

    return False


if __name__ == "__main__":
    print("Waiting for server...")
    time.sleep(2)

    if test_connection():
        print("\n✓ Server is running and responsive!")
        sys.exit(0)
    else:
        print("\n✗ Server is not responding")
        sys.exit(1)
