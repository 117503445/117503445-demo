import consul
c = consul.Consul()
c.kv.put('foo', 'bar')
print(c.kv.get('foo', index=None))