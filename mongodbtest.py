import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.cfjf9.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
"name1":"anurag1",
"email1":"anurag1.icfai2009@gmail.com",
"surname1":"Gupta1"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)