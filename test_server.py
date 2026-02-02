#!/usr/bin/env python3
"""
AML System Server on Port 5001 (for testing)
"""

from aml_system import create_app
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


if __name__ == '__main__':
    app = create_app()
    print("\n" + "=" * 60)
    print("🚀 AML System v10.0 - TESTING ON PORT 5001")
    print("=" * 60)
    print("\nServer: http://127.0.0.1:5001")
    print("=" * 60 + "\n")

    app.run(host='127.0.0.1', port=5001, debug=False, threaded=True)
