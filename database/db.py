from databases import Database
import ormar
import sqlalchemy


database = Database("sqlite:///db.sqlite")
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
