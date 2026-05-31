import uuid

class PortConnection:
    """
    Represents a connection between two ports (edge of graph).
    Ports are referenced by their IDs
    """
    def __init__(self, src_port_id, dst_port_id):
        self.id_ = f"PortConnection_{uuid.uuid4().hex}"
        self.src = src_port_id
        self.dst = dst_port_id
