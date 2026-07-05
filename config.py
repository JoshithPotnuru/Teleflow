import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_ID = int(os.getenv("API_ID") or 0)
    API_HASH = os.getenv("API_HASH")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    SESSION_NAME = os.getenv("SESSION_NAME", "teleflow_session")
    OWNER_ID = int(os.getenv("OWNER_ID") or 0)
