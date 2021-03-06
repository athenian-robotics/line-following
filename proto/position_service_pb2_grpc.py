# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.position_service_pb2 as proto_dot_position__service__pb2


class PositionServiceStub(object):
    def __init__(self, channel):
        """Constructor.
    
        Args:
          channel: A grpc.Channel.
        """
        self.registerClient = channel.unary_unary(
            '/line_following.PositionService/registerClient',
            request_serializer=proto_dot_position__service__pb2.ClientInfo.SerializeToString,
            response_deserializer=proto_dot_position__service__pb2.ServerInfo.FromString,
        )
        self.getPositions = channel.unary_stream(
            '/line_following.PositionService/getPositions',
            request_serializer=proto_dot_position__service__pb2.ClientInfo.SerializeToString,
            response_deserializer=proto_dot_position__service__pb2.Position.FromString,
        )


class PositionServiceServicer(object):
    def registerClient(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getPositions(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PositionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'registerClient': grpc.unary_unary_rpc_method_handler(
            servicer.registerClient,
            request_deserializer=proto_dot_position__service__pb2.ClientInfo.FromString,
            response_serializer=proto_dot_position__service__pb2.ServerInfo.SerializeToString,
        ),
        'getPositions': grpc.unary_stream_rpc_method_handler(
            servicer.getPositions,
            request_deserializer=proto_dot_position__service__pb2.ClientInfo.FromString,
            response_serializer=proto_dot_position__service__pb2.Position.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'line_following.PositionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
