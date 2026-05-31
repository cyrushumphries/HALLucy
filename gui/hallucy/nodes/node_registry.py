import pkgutil
import importlib
import inspect

from hallucy.graph.node import Node

class NodeRegistry:
    """ Automatic register of all nodes defined under hallucy.nodes. """
    def __init__(self):
        self.node_classes = {}  # name -> {class -> category} dictionnary easy iteratable in the node_explorer

    def discover(self, package="hallucy.nodes"):
        """
        Automatically discover and import all modules under the hallucy.nodes.
        These nodes are all subclasses of hallucy.graph.node.
        """
        pkg = importlib.import_module(package)
        for module_info in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + "."):
            module = importlib.import_module(module_info.name)
            for _, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, Node) and obj is not Node:
                    self.node_classes[obj.NAME] = {"cls":obj, "category":obj.CATEGORY}
