'''
Author: HaoTian Qi
Date: 2021-09-25 22:07:07
Description: 
LastEditTime: 2021-09-26 00:23:59
LastEditors: HaoTian Qi
'''

from redis import ResponseError
from redisearch import Client, IndexDefinition, TextField

SCHEMA = (
    TextField("title", weight=5.0),
    TextField("body")
)

client = Client("my-index", port=6380)

definition = IndexDefinition(prefix=['nick:'])

try:
    client.info()
except ResponseError:
    # Index does not exist. We need to create it!
    client.create_index(SCHEMA, definition=definition)

doc = {
    'title': 'RediSearch',
    'body': 'Redisearch adds querying, indexing, and full-text search to Redis'
}
client.redis.hset('nick:1', mapping=doc)

res = client.search("querying")
print(res)