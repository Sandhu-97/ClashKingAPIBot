from pymongo import MongoClient
from database import insertLink
# Connection string
uri = "mongodb+srv://sweash:bot@cluster0.efjiw3q.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(uri)

# Access a specific database
db = client['test']

# Access a specific collection
collection = db['cocs']

# Example: Insert a document

document = collection.find()

