#!/usr/bin/env python3
"""
AML System Server Launcher v5.0
"""

import os
import sys
import logging

# Fix encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf-8', errors='replace')

from aml_system import create_app

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("="*70)
    logger.info("AML AML Case Management System v5.0 - Professional Build")
    logger.info("="*70)

    try:
        app = create_app()
        logger.info("Flask app created successfully")

        host = os.environ.get('FLASK_HOST', '0.0.0.0')
        port = int(os.environ.get('FLASK_PORT', '5000'))
        debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

        logger.info(f"Server: http://{host}:{port}")
        logger.info(f"Database: aml_system.db")
        app.run(
            host=host,
            port=port,
            debug=debug,
            use_reloader=False,
            threaded=True
        )

    except KeyboardInterrupt:
        logger.info("Shutting down...")
    except Exception as e:
        logger.error(f"Error: {e}")
        raise

