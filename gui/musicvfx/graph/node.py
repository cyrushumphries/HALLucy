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

    def __init__(self, node_id):
        self.id = node_id
        self.position = (0, 0)
        self.ports = self.define_ports()

        # assign back-reference TODO check if var is defined in port
        for port in self.ports:
            port.node = self

    def define_ports(self):
        """
        Override in subclasses to define input/output ports.
        Should return a list of NodePort instances.
        """
        return []

    def build_ui(self, dpg_node_id): #TODO rename
        """
        Override in subclasses to build the node's UI.
        """
        pass
