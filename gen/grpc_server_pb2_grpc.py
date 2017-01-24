import grpc

import grpc_server_pb2 as grpc__server__pb2


class FocusLinePositionServerStub(object):
    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.registerClient = channel.unary_unary(
            '/opencv_object_tracking.FocusLinePositionServer/registerClient',
            request_serializer=grpc__server__pb2.ClientInfo.SerializeToString,
            response_deserializer=grpc__server__pb2.ServerInfo.FromString,
        )
        self.getFocusLinePositions = channel.unary_stream(
            '/opencv_object_tracking.FocusLinePositionServer/getFocusLinePositions',
            request_serializer=grpc__server__pb2.ClientInfo.SerializeToString,
            response_deserializer=grpc__server__pb2.FocusLinePosition.FromString,
        )


class FocusLinePositionServerServicer(object):
    def registerClient(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getFocusLinePositions(self, request, context):
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FocusLinePositionServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'registerClient': grpc.unary_unary_rpc_method_handler(
            servicer.registerClient,
            request_deserializer=grpc__server__pb2.ClientInfo.FromString,
            response_serializer=grpc__server__pb2.ServerInfo.SerializeToString,
        ),
        'getFocusLinePositions': grpc.unary_stream_rpc_method_handler(
            servicer.getFocusLinePositions,
            request_deserializer=grpc__server__pb2.ClientInfo.FromString,
            response_serializer=grpc__server__pb2.FocusLinePosition.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'opencv_object_tracking.FocusLinePositionServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
