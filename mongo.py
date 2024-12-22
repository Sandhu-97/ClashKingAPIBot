from pymongo import MongoClient
from database import insertLink, clearTable
from dotenv import load_dotenv
import os
load_dotenv()
# Connection string
uri = os.environ['MONGO_URL']

# Connect to MongoDB
client = MongoClient(uri)

# Access a specific database
db = client['test']

# Access a specific collection
collection = db['cocs']

# Example: Insert a document

document = collection.find()


def load_new_player_links():
    clearTable('LINKS')
    for doc in document:
        insertLink(doc['cocTag'], doc['discordId'])
        print(doc['cocTag'], doc['discordId'], 'inserted')

    print('all inserted')
