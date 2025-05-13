# kafka

## 启动测试环境

```sh
docker compose up -d
```

## quick start

```sh
# 在一个终端中启动消费者
docker compose exec dev uv run consumer.py
# 在另一个终端中启动生产者
docker compose exec dev uv run producer.py
```

## 概念解析

topic - 队列

broker - 一个kafka实例

## 参考链接

<https://kafka.apache.org>

<https://pypi.org/project/kafka-python>

<https://github.com/wurstmeister/kafka-docker>

<https://hub.docker.com/r/wurstmeister/kafka>

<https://www.kingname.info/2020/03/23/operate-kafka-by-python/>
