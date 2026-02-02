"""
Production Configuration for AML Case Management System
Supports both local and cloud deployments
"""

import os
from datetime import timedelta


class Config:
    """Base configuration"""
    DEBUG = False
    TESTING = False

    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///aml_multi_user.db')
    DB_PATH = os.getenv('DB_PATH', 'aml_multi_user.db')

    # Security
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production-xyz123')
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

    # Flask
    JSON_SORT_KEYS = False
    JSONIFY_PRETTYPRINT_REGULAR = False

    # File uploads
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'uploads')


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SESSION_COOKIE_SECURE = True


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DATABASE_URL = 'sqlite:///:memory:'
    SESSION_COOKIE_SECURE = False


# Choose config based on environment
config_name = os.getenv('FLASK_ENV', 'production')
if config_name == 'development':
    config = DevelopmentConfig()
elif config_name == 'testing':
    config = TestingConfig()
else:
    config = ProductionConfig()
