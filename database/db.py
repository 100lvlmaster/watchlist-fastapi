from motor import motor_asyncio
from decouple import config
client = motor_asyncio.AsyncIOMotorClient(config("MONGO_CON"))
bookmarkdb = client.bookmarks
