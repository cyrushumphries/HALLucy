from musicvfx.graph.node import Node
from musicvfx.graph.node_port import NodePort

class Scope(Node):
    NAME = "Scope"
    CATEGORY = "Audio"

    def __init__(self):
        super().__init__()
        self.buffer = []

    def define_ports(self):
        return [
            NodePort(name="in", direction="in", port_type="audio")
        ]

    def build_ui(self):
        pass