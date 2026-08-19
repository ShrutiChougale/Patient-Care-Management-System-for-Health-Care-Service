import os
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-12345')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'dev-jwt-secret-key-998877')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # DB Selection - Single Source of Truth
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = urllib.parse.quote_plus(os.environ.get('DB_PASSWORD', 'shruti2005'))
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '3306')
    DB_NAME = os.environ.get('DB_NAME', 'integrated_patient_care')
    
    MYSQL_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLITE_URI = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'integrated_patient_care.db')}"
    
    # Default to MySQL if USE_MYSQL=true or DATABASE_URL is explicitly set, otherwise fallback to SQLite
    if os.environ.get('USE_MYSQL', 'false').lower() in ['true', '1']:
        SQLALCHEMY_DATABASE_URI = MYSQL_URI
    elif os.environ.get('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    else:
        SQLALCHEMY_DATABASE_URI = SQLITE_URI

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}
