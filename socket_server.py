import socket
import grpc
import concurrent.futures
from grpc_def import grpc_route_pb2 as pb2
from grpc_def import grpc_route_pb2_grpc as pb2_grpc

# Socket server configuration
socket_host = '127.0.0.1'
socket_port = 8080

# gRPC server configuration
grpc_host = '127.0.0.1'
grpc_port = 50051

# Implement your gRPC service
class GrpcRouteService(pb2_grpc.GrpcRouteServicer):
    def GetCategory(self, request, context):
        # Implement your gRPC method logic here
        response = pb2.Category()
        response.message = f"Received gRPC request: {request.message}"
        return response

def run_socket_server():
    socket_host = "127.0.0.1"
    socket_port = 65535
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((socket_host, socket_port))
        server_socket.listen()

        print(f"Socket server is listening on {socket_host}:{socket_port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            # Handle socket communication logic here

def run_grpc_server():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GrpcRouteServicer_to_server(GrpcRouteService(), server)
    server.add_insecure_port(f"{grpc_host}:{grpc_port}")
    print(f"gRPC server is listening on {grpc_host}:{grpc_port}")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    import threading

    # Start the socket server in a separate thread
    socket_server_thread = threading.Thread(target=run_socket_server)
    socket_server_thread.daemon = True
    socket_server_thread.start()

    # Start the gRPC server in the main thread
    run_grpc_server()
