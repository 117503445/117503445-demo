'''
Author: HaoTian Qi
Date: 2021-09-25 22:07:07
Description: 
LastEditTime: 2021-09-25 23:56:18
LastEditors: HaoTian Qi
'''

import time
import random
import redis

r = redis.Redis(host='localhost', port=6379, db=0)


def create_test_data():
    # 2.3 s
    nid = 1
    for i in range(1000):
        x = random.randint(2, 6)
        for _ in range(x):
            r.hset('userid-nickname', f'nickname{nid}', f'userid{i}')
            nid += 1

def query():
    for i in range(1000):
        table = r.hgetall('userid-nickname')
        nicknames = [nick for nick,username in table.items() if username == b'userid653']
        # print(nicknames)

t = time.time()
# create_test_data()
query()
print(time.time()-t)
