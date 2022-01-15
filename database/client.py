from motor import motor_asyncio
from decouple import config
client = motor_asyncio.AsyncIOMotorClient(config("MONGO_CON"))
db_client = client['watchlist']
users = db_client['users']
bookmarks = db_client['bookmarks']
