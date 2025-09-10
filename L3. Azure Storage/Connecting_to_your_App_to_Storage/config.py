import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('hello-world1234.database.windows.net
helloworld12345
') or '[SQL_SERVER_GOES_HERE]'
    SQL_DATABASE = os.environ.get('hello-world-db') or '[SQL_DATABASE_GOES_HERE]'
    SQL_USER_NAME = os.environ.get('Username_11') or '[SQL_USER_NAME_GOES_HERE]'
    SQL_PASSWORD = os.environ.get('Udacity@2025') or '[SQL_PASSWORD_GOES_HERE]'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('helloworld12345') or '[BLOB_ACCOUNT_GOES_HERE]'
    BLOB_STORAGE_KEY = os.environ.get('/6sf0QPfSsI/Ml3dfudx6sjQGFAKIawLZWW4JTgBFYBlaEcLVvzls73JROgsn/QOW54frnWRQWz7+AStWH2VMA==') or '[BLOB_STORAGE_KEY_GOES_HERE]'
    BLOB_CONTAINER = os.environ.get('images') or '[BLOB_CONTAINER_GOES_HERE]'
