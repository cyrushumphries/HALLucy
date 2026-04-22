import dearpygui.dearpygui as dpg

class NodeExplorer:
    """ Displays the registry of available nodes, and allows dragging nodes onto the node_editor. """
    def __init__(self, registry):
        self.registry = registry

    def create(self):
        """Create the DearPyGui node explorer widget."""
        categories = {} # category -> [class, class, ...]
        for node_type in self.registry.node_classes.values():
            #print(f"cls = {node_type["cls"]}")
            #print(f"category= {node_type["category"]}")
            #https://stackoverflow.com/questions/26367812/appending-to-list-in-python-dictionary
            categories.setdefault(node_type["category"],[]).append(node_type["cls"])
       
        with dpg.window(label="Node Explorer", 
                        tag="NodeExplorerWindow"):
            for category, classes in categories.items():
                # Each category is listed under one node
                with dpg.tree_node(label=category):
                    for cls in classes: 
                        # button has drag callback and drag_payload.
                        btn_drag = dpg.add_button(label = cls.NAME, 
                                                  drag_callback = self._drag_callback)
                    
                        # drag_payload associated to button,  drag_data contains the class to instantiate in the node_editor
                        # payload_type needs to be same on drop target
                        with dpg.drag_payload(parent=btn_drag, 
                                              drag_data=cls, 
                                              payload_type="Node"):
                            dpg.add_text(f"Add new {cls.NAME}")

    # -------------------------------------------------------------------------
    # Callbacks
    # -------------------------------------------------------------------------    
    def _drag_callback(sender, app_data, user_data):
        """ Called when selction is dragged"""
        #mot much to do
        pass