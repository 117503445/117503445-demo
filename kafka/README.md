# kafka

## GKD 系列说明

1. 快速把中间件部署起来
2. 快速跑起来简单的例子
3. 然后再慢慢看官方文档

## 部署

编辑 .env 把 hostip 改为自己的

```sh
docker-compose up
```

## 例子

```sh
pip install -r requirements.txt
python consumer.py
python producer.py
```

## 概念解析

// 可能有错

topic - 队列

broker - 一个kafka实例

## 参考链接

<https://kafka.apache.org>

<https://pypi.org/project/kafka-python>

<https://github.com/wurstmeister/kafka-docker>

<https://hub.docker.com/r/wurstmeister/kafka>

<https://www.kingname.info/2020/03/23/operate-kafka-by-python/>
