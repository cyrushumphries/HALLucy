import uuid

class NodePort:
    """
    Represents a single input or output port on a node.
    Many i/o ports can be added to the same node.

    direction: "in" or "out"
    port_type: semantic type (float, audio, event, etc.)
    """

    def __init__(self, name, direction, port_type="any"):
        self.id_ = f"NodePort_{uuid.uuid4().hex}"
        self.name = name
        if direction not in ("in", "out"):
            raise ValueError("direction must be 'in' or 'out'")
        self.direction = direction
        self.port_type = port_type
        self.node = None # will be assigned when added to a Node