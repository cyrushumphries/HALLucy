from musicvfx.graph.node import Node
from musicvfx.graph.node_port import NodePort

class RingModulator(Node):
    NAME = "Ring Modulator"
    CATEGORY = "Audio"

    def __init__(self):
        super().__init__()

    def define_ports(self):
        return [
            NodePort(name="a", direction="in", port_type="audio"),
            NodePort(name="b", direction="in", port_type="audio"),
            NodePort(name="out", direction="out", port_type="audio"),
        ]

    def build_ui(self):
        pass