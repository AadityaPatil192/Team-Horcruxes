from pymongo import MongoClient
from faker import Faker

# Initialize Faker
faker = Faker()

# MongoDB configuration
MONGO_URI = "mongodb+srv://aadityapatil1902:root@cluster0.wvbc0gp.mongodb.net/"  # Replace with your MongoDB URI
DATABASE_NAME = "hr-data"  # Replace with your database name
COLLECTION_NAME = "details"  # Replace with your collection name

# Initialize MongoDB client
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

def add_random_name_to_documents():
    try:
        # Fetch all documents from the collection
        documents = collection.find()

        for document in documents:
            # Generate a random name
            random_name = faker.name()

            # Add the random name to the document
            collection.update_one(
                {'_id': document['_id']},
                {'$set': {'name': random_name}}
            )

        print("Names added to all documents successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    add_random_name_to_documents()
