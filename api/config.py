from os import environ, path
from dotenv import load_dotenv

load_dotenv(path.abspath(".env"))

SECRET_KEY = environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_ECHO = environ.get("SQLALCHEMY_ECHO")
