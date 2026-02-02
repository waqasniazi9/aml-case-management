#!/usr/bin/env python3
"""
Setup Script for AML AML Case Management System
Installs dependencies and initializes the system
"""

import os
import sys
import subprocess


def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully\n")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies\n")
        return False


def create_env_file():
    """Create .env configuration file"""
    print("⚙️  Creating configuration file (.env)...")
    env_content = """# AML AML Case Management System Configuration
FLASK_ENV=production
SECRET_KEY=aml-case-management-secure-key-2024
DEBUG=False
DATABASE_URL=sqlite:///aml_system.db
GITHUB_REPO_OWNER=aml-system
GITHUB_REPO_NAME=aml-case-data
API_PORT=5000
"""
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ Configuration file created (.env)\n")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env: {str(e)}\n")
        return False


def check_python_version():
    """Check if Python version is 3.8 or higher"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(
            f"✅ Python {version.major}.{version.minor}.{version.micro} - OK\n")
        return True
    else:
        print(
            f"❌ Python 3.8+ required (current: {version.major}.{version.minor})\n")
        return False


def main():
    """Main setup function"""
    print("=" * 60)
    print("AML AML Case Management System v3.0")
    print("Setup & Initialization Script")
    print("=" * 60)
    print()

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    # Install dependencies
    if not install_dependencies():
        sys.exit(1)

    # Create config file
    if not create_env_file():
        sys.exit(1)

    # Final instructions
    print("=" * 60)
    print("✅ Setup Complete!")
    print("=" * 60)
    print()
    print("📋 Next Steps:")
    print("1. Run the backend: python aml_system.py")
    print("2. Open HTML file in browser: aml3_system.html")
    print("3. Access API: http://localhost:5000/api")
    print()
    print("📖 Documentation: README.md")
    print("🔒 Edit .env for configuration changes")
    print()


if __name__ == "__main__":
    main()


