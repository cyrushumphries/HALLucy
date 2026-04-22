import dearpygui.dearpygui as dpg

class NodeEditor:
    """
    The main controller for the node editor UI.
    Responsible for:
    - creating the node editor widget
    - creating and drawing nodes
    - handling link creation/deletion
    """

    def __init__(self, graph):
        """ Reference NodeGraph at initialisation """
        self.graph = graph
        self.id_ = None
        # A reference node is needed to calculate the drop position in editor
        # cf issue 2164: https://github.com/hoffstadt/DearPyGui/issues/2164       
        self.ref_node = None

    def create(self):
        """Create the DearPyGui node editor widget."""
        with dpg.window(label="Node Editor", 
                        tag="NodeEditorWindow",
                        no_close=True):
            
            # A group is needed as drop target
            with dpg.group(drop_callback=self._drop_callback, payload_type="Node"):

                # Create the node editor and save its ID
                self.id_ = dpg.add_node_editor(callback=self._link_callback,
                                               delink_callback=self._delink_callback,
                                               user_data="NodeEditor",
                                               minimap=True,
                                               minimap_location=dpg.mvNodeMiniMap_Location_TopRight)

                # Create the reference node and save its ID
                self.ref_node=dpg.add_node(tag="ref-node", 
                                           label="", 
                                           show=False, 
                                           parent=self.id_)

    def draw_node(self, node, pos=(0,0)):
        """ Create and draw a node at position pos inside the node editor. """
        node.position=pos #update pos in node class

        # Create new node. user_data is needed
        with dpg.node(label=node.NAME, 
                      parent=self.id_, 
                      tag=node.id_, 
                      user_data=node.id_, 
                      pos=pos):
            
            for port in node.ports:
                # INPUT PORTS always on the left side
                if port.direction == "in":
                    with dpg.node_attribute(label=port.name, 
                                            attribute_type=dpg.mvNode_Attr_Input,
                                            tag=port.id_, 
                                            user_data=port.id_):
                        dpg.add_text(port.name)          

                # OUTPUT PORTS always on the right side                
                elif port.direction == "out":
                    with dpg.node_attribute(label=port.name, 
                                            attribute_type=dpg.mvNode_Attr_Output,
                                            tag=port.id_,
                                            user_data=port.id_):
                        dpg.add_text(port.name)

    # -------------------------------------------------------------------------
    # Callbacks
    # -------------------------------------------------------------------------
    def _link_callback(self, sender, app_data):
        """ Called when the user connects two ports with a connection. """
        # app_data = (output_attr_id, input_attr_id)
        # DPG is complicated and the doc is not so clear about that: 
        # it should return the "ids defined via the tags given with the "tag=port.port_id",
        # but it returns internal dpg ids the whole time, which need to be tracked/stored in addition, 
        # or the way i figured out, is by using the user_data parameter, when defining the nodes and node attributes
        # pg.node(label=node.name, parent=self.node_editor_id, tag=node.node_id, user_data=node.node_id)
        # That data can be retrieved by doing dpg.get_item_usr_data(dpg_item_id)
        # I want one source of truth, therefore i want to generate my Ids on my own, i dont want to use the dpg IDs
        # since we are using user_data, the "tag" is actually useless (but i kept it)

        out_port_id, in_port_id = app_data
        #print(f"Callback gives the following app_data: {app_data}")
        #print(f"But should be user_data_out:{dpg.get_item_user_data(out_port_id)}")
        #print(f"user_data_in:{And dpg.get_item_user_data(in_port_id)}")

        # Inform the graph of connection
        conn = self.graph.connect(dpg.get_item_user_data(out_port_id), dpg.get_item_user_data(in_port_id))

        # Draw the link visually
        dpg.add_node_link(out_port_id, 
                          in_port_id, 
                          parent=self.id_, 
                          tag=conn.id_, 
                          user_data=conn.id_)

    def _delink_callback(self, sender, app_data):
        """ Called when the user deletes a connection. """
        # app_data = conn_id
        conn_id = dpg.get_item_user_data(app_data)

        # Inform the graph
        self.graph.disconnect(conn_id)
        dpg.delete_item(conn_id)
    
    def _drop_callback(self, sender, app_data, user_data):
        """ Called when a new node is dragged from the node_explorer onto the node_editor. """
        # app_data in drop callback is the drag_data in node_explorer
        # Calculating position within node_editor
        # https://github.com/DataExplorerUser/drag_drop_node_editor/blob/main/drag_and_drop_node_editor_dear_py_gui.py
        # https://github.com/hoffstadt/DearPyGui/issues/2164
        pos = dpg.get_mouse_pos(local=False)
        dpg.show_item(self.ref_node)
        # Let it render once
        dpg.split_frame()
        ref_screen_pos = dpg.get_item_rect_min(self.ref_node)
        ref_grid_pos = dpg.get_item_pos(self.ref_node)
        dpg.hide_item(self.ref_node)
        NODE_PADDING = (8, 8)
        pos[0] = pos[0] - (ref_screen_pos[0] - NODE_PADDING[0]) + ref_grid_pos[0]
        pos[1] = pos[1] - (ref_screen_pos[1] - NODE_PADDING[1]) + ref_grid_pos[1]

        # Add new node to the graph 
        node = self.graph.add_node(app_data)
        # Draw the new node on the editor
        self.draw_node(node, pos=pos)