import logging
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT, MONGODB_URL


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client


async def connect_to_mongo():
    logging.info("Connecting to MongoDB...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    logging.info("Connected to Mongo！")


async def close_mongo_connection():
    logging.info("Closing mongo connection...")
    db.client.close()
    logging.info("Closed mongo connection！")
