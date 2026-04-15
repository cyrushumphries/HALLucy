class PortConnection:
    """
    Represents a connection between two ports (edge of graph).
    """
    def __init__(self, src_port, dst_port):
        self.src = src_port
        self.dst = dst_port
