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
        self.connections = [] # list of PortConnection's #TODO change to id -> PortConnection map
        self._next_id = 1 #TODO replace by uuid

    def add_node(self, node_cls): #TODO rename variable
        node_id = self._next_id
        self._next_id += 1

        node = node_cls(node_id)
        self.nodes[node_id] = node
        return node

    def connect(self, src_port, dst_port):
        conn = PortConnection(src_port, dst_port)
        self.connections.append(conn)  # append to connection register
        return conn
    
    def disconnect(self, src_port, dst_port):
        # remove from connection register TODO change to an id -> connection mapping as in the other pyMusicVFX, makes removal simpler
        self.connections = [
            c for c in self.connections
            if not (c.src == src_port and c.dst == dst_port)
        ]
