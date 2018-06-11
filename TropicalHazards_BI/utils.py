import pymongo


def connect_mongo(engine=pymongo, host='mongo', port=27017):
    mongo_client = engine.MongoClient(host, port)
    mongo_db = mongo_client['main_db']

    return mongo_db
