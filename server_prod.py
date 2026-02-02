#!/usr/bin/env python3
"""
AML System Production Server
Uses Waitress instead of Flask development server
"""

import os
import sys

# Add project to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from aml_system import create_app
    from waitress import serve
    import logging

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    print("=" * 60)
    print("🚀 Starting AML System v10.0 - Production Server")
    print("=" * 60)

    # Create Flask app
    app = create_app()
    logger.info(
        f"✅ Flask app initialized with {len(app.url_map._rules)} routes")

    # Serve with Waitress
    print(f"\n🌐 Server starting on http://127.0.0.1:5000")
    print(f"Dashboard: http://127.0.0.1:5000")
    print(f"Press CTRL+C to stop\n")

    serve(app, host='0.0.0.0', port=5000, threads=4)

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
