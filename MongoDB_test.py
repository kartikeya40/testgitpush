import pymongo

client = pymongo.MongoClient("mongodb+srv://kartikeya40:Kanha#11mongodb@kartikeyacluster.dyydt13.mongodb.net/?retryWrites=true&w=majority")
db = client.test

client

print(db)

d = {'name':'kartikeya','email':'kartikeyasharma40@gmail.com', 'surname': 'sharma'}

db1 = client['mongotest']

col1= db1['test']

col1.insert_one(d)