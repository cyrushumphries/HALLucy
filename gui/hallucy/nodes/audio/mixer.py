from hallucy.graph.node import Node
from hallucy.graph.node_port import NodePort

class Gain(Node):
    NAME = "Gain"
    CATEGORY = "Audio"

    def __init__(self):
        super().__init__()
        self.gain = 1.0  # default gain value

    def define_ports(self):
        return [
            NodePort(name="in", direction="in", port_type="audio"),
            NodePort(name="gain", direction="in", port_type="float"),
            NodePort(name="out", direction="out", port_type="audio"),
        ]

    def build_ui(self):
        pass