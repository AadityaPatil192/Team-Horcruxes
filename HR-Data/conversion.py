import pandas as pd
from pymongo import MongoClient

def csv_to_mongodb(csv_file_path, db_name, collection_name, mongo_uri='mongodb+srv://aadityapatil1902:root@cluster0.wvbc0gp.mongodb.net/'):
    # Read the CSV file using pandas
    df = pd.read_csv(csv_file_path)

    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Convert DataFrame to a dictionary and insert into MongoDB
    data = df.to_dict(orient='records')
    collection.insert_many(data)

    print("Data inserted successfully!")

if __name__ == "__main__":
    # Define the CSV file path, database name, and collection name
    csv_file_path = 'HR_Details.csv'
    db_name = 'hr-data'
    collection_name = 'details'

    # Call the function to insert data into MongoDB
    csv_to_mongodb(csv_file_path, db_name, collection_name)
