import dearpygui.dearpygui as dpg

class NodeEditor:
    """
    The main controller for the node editor UI.
    Responsible for:
    - creating the node editor widget
    - drawing nodes
    - handling link creation/deletion
    """

    def __init__(self, graph):
        self.graph = graph  # reference to NodeGraph
        self.id_ = None

    def create(self):
        """Create the DearPyGui node editor widget."""
        with dpg.window(label="Node Editor", tag="NodeEditorWindow"):
            self.id_ = dpg.add_node_editor(
                callback=self._link_callback,
                delink_callback=self._delink_callback,
                user_data="NodeEditor"
            )

    def draw_node(self, node):
        """
        Draw a node inside the node editor.
        """
        with dpg.node(label=node.NAME, parent=self.id_, tag=node.id_, user_data=node.id_):
            for port in node.ports:
                # INPUT PORTS always on the left side
                if port.direction == "in":
                    with dpg.node_attribute(
                        label=port.name, 
                        attribute_type=dpg.mvNode_Attr_Input, 
                        user_data=port.id_
                    ):
                        dpg.add_text(port.name)          
                    # print("DRAW INPUT:", port.name, "->", port.id_, "->", type(port.id_))

                # OUTPUT PORTS always on the right side                
                elif port.direction == "out":
                    with dpg.node_attribute(
                        label=port.name, 
                        attribute_type=dpg.mvNode_Attr_Output,
                        user_data=port.id_
                    ):
                        dpg.add_text(port.name)
                        # print("DPG attribute tag:", dpg.get_item_alias(port.id_))
                        # print("DPG data:", dpg.get_item_alias(port.id_))


    # -------------------------------------------------------------------------
    # Callbacks
    # -------------------------------------------------------------------------

    def _link_callback(self, sender, app_data):
        """
        Called when the user connects two ports with a connection.
        app_data = (output_attr_id, input_attr_id)
        DPG is complicated and the doc is not so clear about that: 
        it should return the "ids defined via the tags given with the "tag=port.port_id",
        but it returns internal dpg ids the whole time, which need to be tracked/stored in addition, 
        or the way i figured out, is by using the user_data parameter, when defining the nodes and node attributes
        pg.node(label=node.name, parent=self.node_editor_id, tag=node.node_id, user_data=node.node_id)
        That data can be retrieved by doing dpg.get_item_usr_data(dpg_item_id)
        I want one source of truth, therefore i want to generate my Ids on my own, i dont want to use the dpg IDs
        since we are using user_data, the "tag" is actually useless
        """
        print(f"sender is:{sender}")
        print(f"app_data_is:{app_data}")

        out_port_id, in_port_id = app_data
        print(f"user_data_out:{dpg.get_item_user_data(out_port_id)}")
        print(f"user_data_in:{dpg.get_item_user_data(in_port_id)}")

        # Inform the engine graph
        conn = self.graph.connect(dpg.get_item_user_data(out_port_id), dpg.get_item_user_data(in_port_id))

        # Draw the link visually
        dpg.add_node_link(out_port_id, in_port_id, parent=self.id_, tag=conn.id_, user_data=conn.id_)

    def _delink_callback(self, sender, app_data):
        """
        Called when the user deletes a connection.
        app_data = conn_id
        """
        conn_id = dpg.get_item_user_data(app_data)

        # Inform the engine graph
        self.graph.disconnect(conn_id)
        dpg.delete_item(conn_id)