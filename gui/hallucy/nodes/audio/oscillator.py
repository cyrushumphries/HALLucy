from hallucy.graph.node import Node
from hallucy.graph.node_port import NodePort

class Oscillator(Node):
    """
    A simple oscillator node.
    GUI will draw it automatically using NodeEditor.draw_node().
    Rust will eventually compute the actual audio signal.
    """

    NAME = "Oscillator"
    CATEGORY = "Audio"

    def __init__(self):
        super().__init__()
        self.frequency = 440.0   # default parameter
        self.waveform = "sine"   # could be sine/saw/square

    def define_ports(self):
        return [
            NodePort(name="freq", direction="in", port_type="float"),
            NodePort(name="out", direction="out", port_type="audio"),
        ]

    def build_ui(self):
        """
        Optional: GUI-specific widgets inside the node.
        For now, leave empty. NodeEditor will draw ports automatically.
        Later you can add sliders, combo boxes, etc.
        """
        pass
