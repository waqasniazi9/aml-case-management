#!/usr/bin/env python3
"""
Production Server Launcher for AML Case Management System
Works on localhost and cloud platforms
"""

import os
import sys
from aml_system import create_app, logger

if __name__ == '__main__':
    # Environment setup
    environment = os.getenv('FLASK_ENV', 'production')
    port = int(os.getenv('PORT', 5000))
    host = os.getenv('HOST', '0.0.0.0')  # Listen on all interfaces
    debug = environment == 'development'

    logger.info(f"Starting AML System in {environment} mode")
    logger.info(f"Listening on {host}:{port}")

    # Create Flask app
    app = create_app()

    # Production server options
    if environment == 'production':
        # For cloud platforms (Heroku, Railway, Render, etc.)
        try:
            from waitress import serve
            logger.info("Using Waitress WSGI server (production)")
            serve(app, host=host, port=port, threads=4)
        except ImportError:
            # Fallback to Flask development server (not ideal for production)
            logger.warning(
                "Waitress not installed. Using Flask development server.")
            logger.warning("For production, install: pip install waitress")
            app.run(host=host, port=port, debug=False)
    else:
        # Development mode
        app.run(host=host, port=port, debug=debug)
