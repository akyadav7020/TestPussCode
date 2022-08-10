import pymongo
client = pymongo.MongoClient("mongodb://ineuron:ineuron@ac-e5ipuyg-shard-00-00.bgcr20g.mongodb.net:27017,ac-e5ipuyg-shard-00-01.bgcr20g.mongodb.net:27017,ac-e5ipuyg-shard-00-02.bgcr20g.mongodb.net:27017/?ssl=true&replicaSet=atlas-132loy-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
print(db)

d ={
    "name":"sudhanshu",
    "email":"sudhanshu@ineuron.ai",
    "surname": "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)