import couchdb
couch = couchdb.Server('http://admin:admin@localhost:5984/')

db = couch.create('test')

doc = {'foo': 'bar'}
db.save(doc)
id = doc['_id']
print(id, db[id])
