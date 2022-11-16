import os

from nameko.standalone.rpc import ClusterRpcProxy


config = {
    'AMQP_URI': os.getenv("RMQ", "amqp://guest:guest@localhost/"),
}

with ClusterRpcProxy(config) as cluster_rpc:
    cluster_rpc.service.receive_event({'message': 'Hello World!!'})