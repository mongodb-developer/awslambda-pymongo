import os
from pymongo import MongoClient

connect = MongoClient(host=os.environ.get("ATLAS_URI"))

def lambda_handler(event, context):
    # Choose our "sample_restaurants" database and our "restaurants" collection
    database = connect.sample_restaurants
    collection = database.restaurants

    # This is our aggregation pipeline
    pipeline = [

        # We are finding American restaurants in Brooklyn
        {"$match": {"borough": "Brooklyn", "cuisine": "American"}},

        # We only want 5 out of our over 20k+ documents
        {"$limit": 5},

        # We don't want all the details, project what you need
        {"$project": {"_id": 0, "name": 1, "borough": 1, "cuisine": 1}}

    ]

    # This will make our pipeline work
    result = list(collection.aggregate(pipeline))

    # Print our five results
    for restaurant in result:
        print(restaurant)

