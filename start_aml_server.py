#!/usr/bin/env python3
"""
AML Case Management System v10.0 - Server Launcher
Properly handles Flask development server on Windows
"""

import os
import sys
import logging
import threading

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf-8', errors='replace')

from aml_system import create_app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Start the AML system server"""

    logger.info("="*70)
    logger.info("AML Case Management System v10.0 - Production Ready")
    logger.info("="*70)
    logger.info("")
    logger.info("Creating Flask application...")

    try:
        app = create_app()
        logger.info("Flask app created successfully")
    except Exception as e:
        logger.error(f"Failed to create Flask app: {e}")
        sys.exit(1)

    host = os.environ.get('AML_HOST', '0.0.0.0')
    port = int(os.environ.get('AML_PORT', '5000'))
    debug = os.environ.get('AML_DEBUG', 'false').lower() == 'true'

    logger.info("")
    logger.info(f"Server Configuration:")
    logger.info(f"  - Host: {host}")
    logger.info(f"  - Port: {port}")
    logger.info(f"  - Debug: {debug}")
    logger.info(f"  - Dashboard: http://127.0.0.1:{port}")
    logger.info("")
    logger.info("="*70)
    logger.info("Starting AML System Server...")
    logger.info("="*70)
    logger.info("")

    try:
        # Run Flask app with optimal settings for Windows
        logger.info("Flask server is starting...")
        app.run(
            host=host,
            port=port,
            debug=debug,
            use_reloader=False,  # Disable reloader to avoid threading issues on Windows
            threaded=True        # Enable threading for concurrent requests
        )
    except KeyboardInterrupt:
        logger.info("\nServer shutdown requested by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)


if __name__ == '__main__':
    main()
