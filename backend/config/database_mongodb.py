from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from config.setting import settings

client = AsyncIOMotorClient(settings.mongodb_uri)
db = client['vue_music']

async def connect_to_mongo():
    # 創建TTL索引
    await db.files.create_index([("expireAt", 1)], expireAfterSeconds=0)
    await db.comments.create_index([("expireAt", 1)], expireAfterSeconds=0)

def get_db() -> AsyncIOMotorDatabase:
    return db

def close_mongo_connection():
    client.close()