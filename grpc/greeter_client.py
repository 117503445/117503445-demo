# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc

from time import perf_counter

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)

    # response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    # print("Greeter client received: " + response.message)
    # response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
    # print("Greeter client received: " + response.message)

    BATCH_SIZE = 100000

    batchs = []
    for _ in range(700):
        txs = []
        for i in range(BATCH_SIZE):
            txs.append(helloworld_pb2.Tx(data='tx' + str(i)))
        batchs.append(txs)

    t1_start = perf_counter()
    for txs in batchs:
        response = stub.Tx(helloworld_pb2.TxReq(txs=txs))
        print("Greeter client received: " + response.msg)
    t1_stop = perf_counter()
    print("Elapsed time during the whole program in seconds:",
                                        t1_stop-t1_start)


if __name__ == '__main__':
    logging.basicConfig()
    run()
