#!/usr/bin/env python3
"""
AML System Server v10.0
"""

import os
import sys
import logging

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from aml_system import create_app

    logger.info("=" * 60)
    logger.info("🚀 Starting AML System v10.0")
    logger.info("=" * 60)

    # Create the Flask app
    app = create_app()
    logger.info(f"✅ Flask app created with {len(app.url_map._rules)} routes")

    # Run the server
    logger.info("🌐 Server starting on http://0.0.0.0:5000")
    logger.info("Dashboard: http://127.0.0.1:5000")

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True
    )

except Exception as e:
    logger.error(f"Error starting server: {e}", exc_info=True)
    sys.exit(1)
