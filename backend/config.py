import os
from dotenv import load_dotenv

# Load environment variables from .env file.
load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    #OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENWEATHER_API_KEY: str = os.getenv("OPENWEATHER_API_KEY", "")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Add this line for Gemini

settings = Settings()
