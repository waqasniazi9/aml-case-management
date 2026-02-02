#!/usr/bin/env python3
"""Startup script for AML System Server"""

import os
import sys
import logging

# Suppress log output to avoid PowerShell errors
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

# Import the app
try:
    from aml_system import create_app
    print("Importing aml_system... OK")

    app = create_app()
    print("Creating Flask app... OK")

    # Start the server
    print("Starting server on http://0.0.0.0:5000")
    print("=" * 60)

    app.run(debug=False, host='0.0.0.0', port=5000,
            use_reloader=False, threaded=True)

except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)
