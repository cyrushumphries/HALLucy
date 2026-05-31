import uuid

class Node:
    """
    A basic node class for all the nodes to be placed on the GUI.

    Subclasses should override:
    - NAME
    - CATEGORY
    - define_ports()
    - build_ui()
    """

    NAME = "Node"
    CATEGORY = "generic"

    def __init__(self):
        self.calculate_id()
        self.position = (0, 0)
        self.ports = self.define_ports()

        # update back-reference in Port
        for port in self.ports:
            port.node = self

    def define_ports(self):
        """
        Override in subclasses to define input/output ports.
        Should return a list of NodePort instances.
        """
        return []

    def build_ui(self): #TODO rename
        """
        Override in subclasses to build the node's UI.
        """
        pass

    def calculate_id(self):
        self.id_ = f"Node_{uuid.uuid4().hex}"
