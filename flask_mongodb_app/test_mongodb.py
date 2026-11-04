from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

mongo_url = os.getenv("MONGO_URL")

client = MongoClient(
    mongo_url,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=15000
)

try:
    client.admin.command("ping")
    print("MongoDB Atlas connection successful!")

except Exception as e:
    print("MongoDB connection failed!")
    print(e)

finally:
    client.close()