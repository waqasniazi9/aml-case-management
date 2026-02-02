#!/usr/bin/env python3
"""
AML Case Management System - Debug Server Launcher
"""

import os
import sys
import logging
import traceback

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(
        sys.stderr.buffer, encoding='utf-8', errors='replace')

# Configure logging to both console and file
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('aml_server_debug.log', mode='w', encoding='utf-8')
    ]
)

logger = logging.getLogger(__name__)


def run_server():
    """Run the AML system server with full error handling"""
    try:
        logger.info("="*70)
        logger.info("AML Case Management System v10.0 - DEBUG MODE")
        logger.info("="*70)
        logger.info("")

        logger.info("Stage 1: Importing aml_system...")
        from aml_system import create_app
        logger.info("SUCCESS: aml_system imported")

        logger.info("Stage 2: Creating Flask app...")
        app = create_app()
        logger.info("SUCCESS: Flask app created")

        logger.info("Stage 3: Configuring app...")
        app.config['ENV'] = 'production'
        app.config['TESTING'] = False
        logger.info("SUCCESS: App configured")

        logger.info("")
        logger.info("="*70)
        logger.info("Starting Flask server...")
        logger.info("Dashboard: http://127.0.0.1:5000")
        logger.info("Press Ctrl+C to stop")
        logger.info("="*70)
        logger.info("")

        # Add some debugging to Flask
        @app.before_request
        def log_request():
            logger.info(f"REQUEST: {request.method} {request.path}")

        @app.after_request
        def log_response(response):
            logger.info(f"RESPONSE: {response.status_code}")
            return response

        logger.info("Starting server...")
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=False,
            use_reloader=False,
            threaded=False
        )

    except KeyboardInterrupt:
        logger.info("\nServer stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"ERROR: {e}")
        logger.error(traceback.format_exc())
        sys.exit(1)


if __name__ == '__main__':
    run_server()
