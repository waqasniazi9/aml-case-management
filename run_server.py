#!/usr/bin/env python3
"""
AML System v10.0 - Threaded Server
Works around Flask dev server socket issues on Windows
"""

import logging
from werkzeug.serving import make_server
from aml_system import create_app
import os
import sys
import socket
import threading
import time
from functools import wraps

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_server():
    """Run the Flask server in a thread"""
    app = create_app()

    logger.info("=" * 60)
    logger.info("🚀 AML System v10.0 - Starting Server")
    logger.info("=" * 60)
    logger.info(f"📍 Dashboard: http://127.0.0.1:5000")
    logger.info(f"API Routes: {len(app.url_map._rules)}")
    logger.info("=" * 60)

    # Create Werkzeug server
    server = make_server('0.0.0.0', 5000, app, threaded=True)

    logger.info("\n✅ Server ready and listening on http://0.0.0.0:5000\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("\n✅ Server stopped")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == '__main__':
    run_server()
