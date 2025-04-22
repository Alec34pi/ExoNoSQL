from pymongo import MongoClient

uri = "mongodb://admin:MotDePasseTropSecure@localhost:27017/?authSource=admin"
client = MongoClient(uri)


db = client["testdb"]
collection = db["users"]

collection.insert_one({"name": "Alice", "age": 30})
print(list(collection.find()))
