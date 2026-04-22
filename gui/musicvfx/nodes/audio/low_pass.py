from musicvfx.graph.node import Node
from musicvfx.graph.node_port import NodePort

class LowPass(Node):
    NAME = "Low Pass"
    CATEGORY = "Audio"

    def __init__(self):
        super().__init__()
        self.cutoff = 1000.0  # default cutoff frequency

    def define_ports(self):
        return [
            NodePort(name="in", direction="in", port_type="audio"),
            NodePort(name="cutoff", direction="in", port_type="float"),
            NodePort(name="out", direction="out", port_type="audio"),
        ]

    def build_ui(self):
        pass