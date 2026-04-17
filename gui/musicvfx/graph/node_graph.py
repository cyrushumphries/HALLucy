from .port_connection import PortConnection
from .node import Node

class NodeGraph:
    """
    The GUI-side graph model.

    Stores:
    - nodes
    - ports
    - connections

    Connections are between ports of nodes, not directly between nodes.
    """

    def __init__(self):
        self.nodes = {} # map of id -> Node object
        self.ports = {} # map of id -> NodePort object
        self.connections = {} # map of id -> PortConnection object

    def add_node(self, node_class):
        node = node_class()
        if node.id_ not in self.nodes:
            self.nodes[node.id_] = node # add new node to register
            for port in node.ports:
                self._add_port(port)
        return node
        
    def remove_node(self, id_):
        if id_ in self.nodes:
            node_to_remove = self.nodes[id_]
            for port in node_to_remove.ports:
                self._remove_port(port.id_)
            del self.nodes[id_]

    def _add_port(self, port_class):
        if port_class.id_ not in self.ports:
            self.ports[port_class.id_] = port_class

    def _remove_port(self, id_):
        if id_ in self.ports:
            # Remove port from register
            del self.ports[id_]

            # now check if connections are using the port and delete those connections
            to_delete = [
                connection_id for connection_id, connection in self.connections.items()
                if connection.src == id_ or connection.dst ==id_
            ]
            for connection_id in to_delete:
                del self.connections[connection_id]

    def connect(self, src_port_id, dst_port_id):
        if (src_port_id in self.ports) and (dst_port_id in self.ports):
            conn = PortConnection(src_port_id, dst_port_id)
            self.connections[conn.id_] = conn  # add new PortConnection to register
            return conn
    
    def disconnect(self, connection_id):
        if connection_id in self.connections:
            del self.connections[connection_id]
