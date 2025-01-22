from pymongo import MongoClient
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str

    class Config:
        env_file = ".env"

try:
    settings = Settings()
    print(".env file loaded successfully.")
except Exception as e:
    print(f"Error loading .env file: {e}")

# MongoDB client and database setup
try:
    client = MongoClient(settings.MONGO_URI)
    db = client.blog_database
    blog_collection = db.blogs
    print("Connected to MongoDB successfully.")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
