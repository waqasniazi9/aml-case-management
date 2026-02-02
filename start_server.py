#!/usr/bin/env python3
"""Enhanced server startup for AML System"""

import os
import sys
import time
import logging
from threading import Thread

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s',
    stream=sys.stdout
)

log = logging.getLogger(__name__)


def main():
    try:
        log.info("=" * 70)
        log.info("AML AML Case Management System v3.5 - Starting")
        log.info("=" * 70)

        log.info("Step 1: Importing aml_system module...")
        from aml_system import create_app
        log.info("[OK] Import successful")

        log.info("Step 2: Creating Flask application...")
        app = create_app()
        log.info("[OK] Flask app created successfully")

        log.info("Step 3: Configuring Flask...")
        app.config['ENV'] = 'production'
        app.config['TESTING'] = False
        log.info("[OK] Flask configured")

        log.info("=" * 70)
        log.info("Starting Flask development server...")
        log.info("API available at: http://localhost:5000")
        log.info("Press Ctrl+C to stop the server")
        log.info("=" * 70)

        # Run with specific settings
        # Using non-threaded mode and 0.0.0.0 for better Windows compatibility
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=False,
            use_reloader=False,
            threaded=False,
            use_debugger=False
        )

    except KeyboardInterrupt:
        log.info("\n" + "=" * 70)
        log.info("Server stopped by user")
        log.info("=" * 70)
        sys.exit(0)
    except Exception as e:
        log.error("=" * 70)
        log.error(f"FATAL ERROR: {e}")
        log.error("=" * 70)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

