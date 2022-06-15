import etcd3

etcd = etcd3.client()

etcd.put('bar', 'doot')
print(etcd.get('bar'))
