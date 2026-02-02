#!/usr/bin/env python3
"""
Simple test server to debug connectivity issues
"""
import sys
import os
import socket
import threading
import time

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf-8', errors='replace')

# Test if port is free


def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('127.0.0.1', port))
    sock.close()
    return result != 0

# Test direct socket binding


def test_socket_binding():
    print("Testing socket binding...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.bind(('127.0.0.1', 5000))
        sock.listen(1)
        print(f"✅ Socket bound successfully to 127.0.0.1:5000")
        print(f"✅ Socket listening...")
        sock.close()
        return True
    except Exception as e:
        print(f"❌ Socket binding failed: {e}")
        return False

# Now try Flask


def test_flask():
    print("\nTesting Flask server...")
    from aml_system import create_app

    app = create_app()
    print(f"✅ Flask app created")

    # Test with test_client
    print("\nTesting Flask with test_client...")
    try:
        client = app.test_client()
        response = client.get('/')
        print(f"✅ Flask test_client works: Status {response.status_code}")
        print(f"   Content length: {len(response.data)} bytes")
    except Exception as e:
        print(f"❌ Flask test_client failed: {e}")
        return False

    # Now try running the server
    print("\nStarting Flask development server on 0.0.0.0:5000...")
    print("Listen for requests from another terminal...")

    try:
        # Use threading to avoid blocking
        def run_server():
            app.run(
                host='0.0.0.0',
                port=5000,
                debug=False,
                use_reloader=False,
                threaded=True
            )

        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()

        # Wait for server to start
        time.sleep(3)

        # Check if server is accepting connections
        print("\nChecking if server is accepting connections...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', 5000))
        sock.close()

        if result == 0:
            print(f"✅ Server IS accepting connections on 127.0.0.1:5000")
            print("\nServer is running. Press Ctrl+C to stop...")
            server_thread.join()
        else:
            print(
                f"❌ Server is NOT accepting connections (error code: {result})")

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    print("="*60)
    print("AML System Server Connectivity Test")
    print("="*60)

    if not test_socket_binding():
        print("\nPort 5000 might be in use or reserved. Exiting.")
        sys.exit(1)

    test_flask()
