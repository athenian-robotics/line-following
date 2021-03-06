import logging
import time

import grpc
from arc852.grpc_support import GenericServer
from arc852.utils import setup_logging
from concurrent import futures

from proto.position_service_pb2 import Position
from proto.position_service_pb2 import PositionServiceServicer
from proto.position_service_pb2 import ServerInfo
from proto.position_service_pb2 import add_PositionServiceServicer_to_server

logger = logging.getLogger(__name__)


class PositionServer(PositionServiceServicer, GenericServer):
    def __init__(self, port=None):
        super(PositionServer, self).__init__(port=port, desc="position server")
        self.grpc_server = None

    def registerClient(self, request, context):
        logger.info("Connected to %s client %s [%s]", self.desc, context.peer(), request.info)
        return ServerInfo(info="Server invoke count {0}".format(self.increment_cnt()))

    def getPositions(self, request, context):
        client_info = request.info
        return self.currval_generator(context.peer())

    def _init_values_on_start(self):
        self.write_position(False, -1, -1, -1, -1, -1)

    def _start_server(self):
        logger.info("Starting gRPC %s listening on %s", self.desc, self.hostname)
        self.grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        add_PositionServiceServicer_to_server(self, self.grpc_server)
        self.grpc_server.add_insecure_port(self.hostname)
        self.grpc_server.start()
        try:
            while not self.stopped:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()

    def write_position(self, in_focus, mid_offset, degrees, mid_line_cross, width, middle_inc):
        if not self.stopped:
            self.set_currval(Position(id=self.id,
                                      in_focus=in_focus,
                                      mid_offset=mid_offset,
                                      degrees=degrees,
                                      mid_line_cross=mid_line_cross,
                                      width=width,
                                      middle_inc=middle_inc))
            self.id += 1


def main():
    setup_logging()
    with PositionServer() as server:
        for i in range(100):
            server.write_position(in_focus=True if i % 2 == 0 else False,
                                  mid_offset=i,
                                  degrees=i + 1,
                                  mid_line_cross=i + 2,
                                  width=i + 3,
                                  middle_inc=i + 4)
            time.sleep(1)


if __name__ == "__main__":
    main()
