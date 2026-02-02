#!/usr/bin/env python3
"""
AML System Online Setup - Automatic ngrok Tunnel
Makes your AML system publicly accessible
"""

import subprocess
import time
import requests
import os
import sys
from pathlib import Path


def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")


def print_success(text):
    """Print success message"""
    print(f"✅ {text}")


def print_error(text):
    """Print error message"""
    print(f"❌ {text}")


def print_info(text):
    """Print info message"""
    print(f"ℹ️  {text}")


def start_server():
    """Start the Flask server"""
    print_info("Starting AML Flask server on port 5000...")
    try:
        subprocess.Popen(
            [sys.executable, "start_server.py"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(3)
        print_success("Flask server started")
        return True
    except Exception as e:
        print_error(f"Failed to start server: {e}")
        return False


def check_server():
    """Check if server is responding"""
    try:
        r = requests.get("http://127.0.0.1:5000/", timeout=3)
        if r.status_code == 200:
            print_success("Server is responding (HTTP 200)")
            return True
    except:
        pass
    print_info("Server is starting up...")
    return False


def start_ngrok():
    """Start ngrok tunnel"""
    ngrok_path = Path("C:/Users/OTS/AppData/Local/Programs/ngrok/ngrok.exe")
    if not ngrok_path.exists():
        print_error("ngrok not found!")
        return False

    print_info("Starting ngrok tunnel...")
    try:
        subprocess.Popen(
            [str(ngrok_path), "http", "5000"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(3)
        print_success("ngrok tunnel started")
        return True
    except Exception as e:
        print_error(f"Failed to start ngrok: {e}")
        return False


def get_ngrok_url():
    """Get the public URL from ngrok"""
    for attempt in range(15):
        try:
            r = requests.get("http://localhost:4040/api/tunnels", timeout=2)
            data = r.json()
            if data.get("tunnels") and len(data["tunnels"]) > 0:
                url = data["tunnels"][0].get("public_url")
                if url:
                    return url
        except:
            pass

        print_info(f"Waiting for ngrok tunnel... ({attempt+1}/15)")
        time.sleep(1)

    return None


def main():
    """Main function"""
    print_header("AML SYSTEM - ONLINE SETUP WITH ngrok")

    # Step 1: Start server
    print_info("Step 1: Starting Flask server...")
    if not start_server():
        print_error("Could not start server")
        return

    # Step 2: Check server
    print_info("Step 2: Verifying server connection...")
    check_server()
    time.sleep(2)

    # Step 3: Start ngrok
    print_info("Step 3: Starting ngrok tunnel...")
    if not start_ngrok():
        print_error("Could not start ngrok")
        return

    # Step 4: Get URL
    print_info("Step 4: Retrieving public URL...")
    url = get_ngrok_url()

    if url:
        print_header("🎉 YOUR AML SYSTEM IS NOW ONLINE!")
        print(f"📱 Public URL:  {url}")
        print(f"🔐 Username:    admin")
        print(f"🔐 Password:    admin123")
        print(f"⏱️  Valid for:    2 hours (free tier)")
        print(f"👥 Share URL:   Anyone can access it!")
        print("\n" + "="*60)
        print("  Keep this window open to maintain the connection")
        print("="*60 + "\n")
        print_success("System is live and accessible!")

        # Keep running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print_info("Shutting down...")
    else:
        print_error("Could not retrieve ngrok URL after multiple attempts")


if __name__ == "__main__":
    main()
