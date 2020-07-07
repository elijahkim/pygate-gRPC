# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: reputation_rpc.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='reputation_rpc.proto',
  package='reputation.rpc',
  syntax='proto3',
  serialized_options=b'Z-github.com/textileio/powergate/reputation/rpc',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14reputation_rpc.proto\x12\x0ereputation.rpc\")\n\nMinerScore\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\"-\n\x10\x41\x64\x64SourceRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05maddr\x18\x02 \x01(\t\"\x13\n\x11\x41\x64\x64SourceResponse\"$\n\x13GetTopMinersRequest\x12\r\n\x05limit\x18\x01 \x01(\x05\"F\n\x14GetTopMinersResponse\x12.\n\ntop_miners\x18\x01 \x03(\x0b\x32\x1a.reputation.rpc.MinerScore2\xbd\x01\n\nRPCService\x12R\n\tAddSource\x12 .reputation.rpc.AddSourceRequest\x1a!.reputation.rpc.AddSourceResponse\"\x00\x12[\n\x0cGetTopMiners\x12#.reputation.rpc.GetTopMinersRequest\x1a$.reputation.rpc.GetTopMinersResponse\"\x00\x42/Z-github.com/textileio/powergate/reputation/rpcb\x06proto3'
)




_MINERSCORE = _descriptor.Descriptor(
  name='MinerScore',
  full_name='reputation.rpc.MinerScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='reputation.rpc.MinerScore.addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='reputation.rpc.MinerScore.score', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=81,
)


_ADDSOURCEREQUEST = _descriptor.Descriptor(
  name='AddSourceRequest',
  full_name='reputation.rpc.AddSourceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='reputation.rpc.AddSourceRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='maddr', full_name='reputation.rpc.AddSourceRequest.maddr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=128,
)


_ADDSOURCERESPONSE = _descriptor.Descriptor(
  name='AddSourceResponse',
  full_name='reputation.rpc.AddSourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=149,
)


_GETTOPMINERSREQUEST = _descriptor.Descriptor(
  name='GetTopMinersRequest',
  full_name='reputation.rpc.GetTopMinersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='reputation.rpc.GetTopMinersRequest.limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=151,
  serialized_end=187,
)


_GETTOPMINERSRESPONSE = _descriptor.Descriptor(
  name='GetTopMinersResponse',
  full_name='reputation.rpc.GetTopMinersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='top_miners', full_name='reputation.rpc.GetTopMinersResponse.top_miners', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=259,
)

_GETTOPMINERSRESPONSE.fields_by_name['top_miners'].message_type = _MINERSCORE
DESCRIPTOR.message_types_by_name['MinerScore'] = _MINERSCORE
DESCRIPTOR.message_types_by_name['AddSourceRequest'] = _ADDSOURCEREQUEST
DESCRIPTOR.message_types_by_name['AddSourceResponse'] = _ADDSOURCERESPONSE
DESCRIPTOR.message_types_by_name['GetTopMinersRequest'] = _GETTOPMINERSREQUEST
DESCRIPTOR.message_types_by_name['GetTopMinersResponse'] = _GETTOPMINERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MinerScore = _reflection.GeneratedProtocolMessageType('MinerScore', (_message.Message,), {
  'DESCRIPTOR' : _MINERSCORE,
  '__module__' : 'reputation_rpc_pb2'
  # @@protoc_insertion_point(class_scope:reputation.rpc.MinerScore)
  })
_sym_db.RegisterMessage(MinerScore)

AddSourceRequest = _reflection.GeneratedProtocolMessageType('AddSourceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDSOURCEREQUEST,
  '__module__' : 'reputation_rpc_pb2'
  # @@protoc_insertion_point(class_scope:reputation.rpc.AddSourceRequest)
  })
_sym_db.RegisterMessage(AddSourceRequest)

AddSourceResponse = _reflection.GeneratedProtocolMessageType('AddSourceResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDSOURCERESPONSE,
  '__module__' : 'reputation_rpc_pb2'
  # @@protoc_insertion_point(class_scope:reputation.rpc.AddSourceResponse)
  })
_sym_db.RegisterMessage(AddSourceResponse)

GetTopMinersRequest = _reflection.GeneratedProtocolMessageType('GetTopMinersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTOPMINERSREQUEST,
  '__module__' : 'reputation_rpc_pb2'
  # @@protoc_insertion_point(class_scope:reputation.rpc.GetTopMinersRequest)
  })
_sym_db.RegisterMessage(GetTopMinersRequest)

GetTopMinersResponse = _reflection.GeneratedProtocolMessageType('GetTopMinersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTOPMINERSRESPONSE,
  '__module__' : 'reputation_rpc_pb2'
  # @@protoc_insertion_point(class_scope:reputation.rpc.GetTopMinersResponse)
  })
_sym_db.RegisterMessage(GetTopMinersResponse)


DESCRIPTOR._options = None

_RPCSERVICE = _descriptor.ServiceDescriptor(
  name='RPCService',
  full_name='reputation.rpc.RPCService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=262,
  serialized_end=451,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddSource',
    full_name='reputation.rpc.RPCService.AddSource',
    index=0,
    containing_service=None,
    input_type=_ADDSOURCEREQUEST,
    output_type=_ADDSOURCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetTopMiners',
    full_name='reputation.rpc.RPCService.GetTopMiners',
    index=1,
    containing_service=None,
    input_type=_GETTOPMINERSREQUEST,
    output_type=_GETTOPMINERSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RPCSERVICE)

DESCRIPTOR.services_by_name['RPCService'] = _RPCSERVICE

# @@protoc_insertion_point(module_scope)
