from hallucy.graph.node import Node
from hallucy.graph.node_port import NodePort

class Output(Node):
    NAME = "Output"
    CATEGORY = "Audio"

    def __init__(self):
        super().__init__()

    def define_ports(self):
        return [
            NodePort(name="in", direction="in", port_type="audio")
        ]

    def build_ui(self):
        pass