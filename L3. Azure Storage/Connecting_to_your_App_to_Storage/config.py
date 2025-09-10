import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'hello-world1234.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'hello-world-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'Username_11'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Username_11
Udacity@2025
'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'helloworld12345'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or '/6sf0QPfSsI/Ml3dfudx6sjQGFAKIawLZWW4JTgBFYBlaEcLVvzls73JROgsn/QOW54frnWRQWz7+AStWH2VMA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
