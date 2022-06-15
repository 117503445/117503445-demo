import nacos

# Both HTTP/HTTPS protocols are supported, if not set protocol prefix default is HTTP, and HTTPS with no ssl check(verify=False)
# "192.168.3.4:8848" or "https://192.168.3.4:443" or "http://192.168.3.4:8848,192.168.3.5:8848" or "https://192.168.3.4:443,https://192.168.3.5:443"
SERVER_ADDRESSES = "http://localhost:8848"
NAMESPACE = "test"

# no auth mode
client = nacos.NacosClient(
    SERVER_ADDRESSES, namespace=NAMESPACE, username="nacos", password="nacos")
# auth mode
#client = nacos.NacosClient(SERVER_ADDRESSES, namespace=NAMESPACE, username="nacos", password="nacos")


# get config
data_id = "mydata"
group = "mygroup"

print(client.publish_config(data_id,group,'hello'))
# 发布后暂时拿不到配置
print(client.get_config(data_id, group))


def main():
    pass


if __name__ == '__main__':
    main()
