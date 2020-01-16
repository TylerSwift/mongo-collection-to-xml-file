from pymongo import MongoClient


class MongoDatabase:

    def __init__(self, hostname, portnumber):
        self.mongo_client = MongoClient(hostname, portnumber)

    def get_mongo_collection(self, database_name, collection_name):
        db = self.mongo_client(database_name)
        return db[collection_name]

