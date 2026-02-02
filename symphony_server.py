#!/usr/bin/env python3
"""
Symphony AML Server Launcher
Advanced Financial Crime Detection Platform
Built on Flask + SQLite with Vertical AI Pattern
"""

import os
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def banner():
    """Display startup banner"""
    try:
        print("\n")
        print("=" * 80)
        print(" " * 15 + "SYMPHONY AML - Financial Crime Detection Platform")
        print(" " * 10 + "Advanced Investigation & Compliance Management System")
        print("=" * 80)
        print("")
        print("Features:")
        print("  * Real-time fraud detection with AI")
        print("  * Advanced case & enquiry management")
        print("  * Complete audit trail for compliance")
        print("  * Multi-user investigation platform")
        print("")
        print("=" * 80)
        print("\n")
    except:
        # Fallback if print fails
        print("SYMPHONY AML - Financial Crime Detection Platform\n")


def main():
    try:
        banner()

        logger.info("=" * 80)
        logger.info("Starting Symphony AML Server Startup Sequence")
        logger.info("=" * 80)

        # Step 1: Import modules
        logger.info("Step 1 - Loading application modules...")
        try:
            from aml_system import create_app
            logger.info("   SUCCESS - Application modules imported")
        except ImportError as e:
            logger.error(f"   ERROR - Failed to import modules: {e}")
            return 1

        # Step 2: Create Flask app
        logger.info("Step 2 - Initializing Flask application...")
        try:
            app = create_app()
            logger.info("   SUCCESS - Flask application created")
        except Exception as e:
            logger.error(f"   ERROR - Failed to create app: {e}")
            return 1

        # Step 3: Verify dashboard exists
        logger.info("Step 3 - Verifying dashboard files...")
        dashboard_file = Path("symphony_dashboard.html")
        if dashboard_file.exists():
            size = dashboard_file.stat().st_size
            logger.info(
                f"   SUCCESS - Symphony AI dashboard found ({size:,} bytes)")
        else:
            logger.warning(
                f"   WARNING - symphony_dashboard.html not found, will use fallback")

        # Step 4: Check database
        logger.info("Step 4 - Verifying database...")
        db_file = Path("aml_multi_user.db")
        if db_file.exists():
            size = db_file.stat().st_size
            logger.info(f"   SUCCESS - Database found ({size:,} bytes)")
        else:
            logger.info("   INFO - Creating new database...")

        # Step 5: Register routes
        logger.info("Step 5 - Analyzing registered routes...")
        route_count = 0
        for rule in app.url_map.iter_rules():
            if rule.endpoint != 'static':
                route_count += 1
        logger.info(f"   SUCCESS - {route_count} API routes registered")

        # Step 6: Start server
        logger.info("Step 6 - Starting Flask development server...")
        logger.info("=" * 80)
        logger.info("")
        logger.info("SERVER INFORMATION:")
        logger.info(f"   URL:  http://127.0.0.1:5000")
        logger.info(f"   Host: 0.0.0.0")
        logger.info(f"   Port: 5000")
        logger.info("")
        logger.info("FEATURES AVAILABLE:")
        logger.info("   * Dashboard: http://127.0.0.1:5000/")
        logger.info("   * Case Management: API endpoints")
        logger.info("   * Enquiry Management: API endpoints")
        logger.info("   * Audit Trail: Complete tracking")
        logger.info("   * Analytics: Real-time metrics")
        logger.info("")
        logger.info("DEFAULT CREDENTIALS:")
        logger.info("   Create account on login screen")
        logger.info("")
        logger.info("Press CTRL+C to stop the server")
        logger.info("=" * 80)
        logger.info("")

        # Run the app
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=False,
            threaded=True,
            use_reloader=False
        )

    except KeyboardInterrupt:
        logger.info("Server shutdown requested by user")
        return 0
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
