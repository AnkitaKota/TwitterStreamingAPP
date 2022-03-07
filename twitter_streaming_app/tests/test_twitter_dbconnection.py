from pymongo import MongoClient

from pytest_mock_resources import create_mongo_fixture

mongo = create_mongo_fixture()

#connectionString = 'mongodb+srv://' + db_user_name + ':' + db_user_password + '@cluster0.nf7ja.mongodb.net/' + db_name + '?retryWrites=true&w=majority'

def test_create_custom_connection(mongo):
    client = MongoClient(**mongo.pmr_credentials.as_mongo_kwargs())
    db = client[mongo.config["database"]]

    collection = db["customers"]
    to_insert = [
        {"name": "John"},
        {"name": "Viola"},
    ]
    collection.insert_many(to_insert)

    result = collection.find().sort("name")
    returned = [row for row in result]

    assert returned == to_insert
