import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "sofar-secret-key")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///sofar.db")
