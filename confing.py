TOKEN = 8515512057:AAGODA4CJ3MEAWO8QgG3PYiDB6OlWUpnNV4
import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "sofar-secret-key")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///sofar.db")
