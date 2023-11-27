
from datetime import timedelta
import os
from dotenv import load_dotenv 

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(basedir, '.env'))

class Config():

    """
    Create Config class which will setup our configuration variables.
    Using Environment variables where avaialbe other create config variables.
    """
    #regular config for Flask App
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')

    #config if you are connecting a database
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'anything it needs to be a string'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #we don't want a message every time our database is changed
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)