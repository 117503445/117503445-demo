# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x12\nhelloworld\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x12\n\x02Tx\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"$\n\x05TxReq\x12\x1b\n\x03txs\x18\x01 \x03(\x0b\x32\x0e.helloworld.Tx\"\x15\n\x06TxResp\x12\x0b\n\x03msg\x18\x01 \x01(\t2\xbd\x01\n\x07Greeter\x12>\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12\x43\n\rSayHelloAgain\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12-\n\x02Tx\x12\x11.helloworld.TxReq\x1a\x12.helloworld.TxResp\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helloworld_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'
  _globals['_HELLOREQUEST']._serialized_start=32
  _globals['_HELLOREQUEST']._serialized_end=60
  _globals['_HELLOREPLY']._serialized_start=62
  _globals['_HELLOREPLY']._serialized_end=91
  _globals['_TX']._serialized_start=93
  _globals['_TX']._serialized_end=111
  _globals['_TXREQ']._serialized_start=113
  _globals['_TXREQ']._serialized_end=149
  _globals['_TXRESP']._serialized_start=151
  _globals['_TXRESP']._serialized_end=172
  _globals['_GREETER']._serialized_start=175
  _globals['_GREETER']._serialized_end=364
# @@protoc_insertion_point(module_scope)
