import dearpygui.dearpygui as dpg
from musicvfx.graph.node_graph import NodeGraph
from musicvfx.widgets.node_editor import NodeEditor
from musicvfx.widgets.node_explorer import NodeExplorer
from musicvfx.nodes.audio.oscillator import Oscillator
from musicvfx.nodes.node_registry import NodeRegistry

# Calculate default layout (3 docks, left top half, left bottom half, right ) (left 20%, right 80%)
# This fixes the layout to a static layout, as soon as the windows is reseized, the default layout will be back
def on_viewport_resize():
    w = dpg.get_viewport_client_width()
    h = dpg.get_viewport_client_height()
    # print(f"Viewport resized → {w} x {h}")
    left_width = int(w*0.20)
    left_height = int(h*0.5)
    right_width = int(w*0.8)
    right_height = h
    properties_coord = (0,0)
    explorer_coord = (0,left_height)
    editor_coord = (left_width,0)
    dpg.set_item_height(item="PropertiesWindow",height=left_height)
    dpg.set_item_width(item="PropertiesWindow",width=left_width)
    dpg.set_item_pos(item="PropertiesWindow",pos=properties_coord)
    dpg.set_item_height(item="NodeExplorerWindow",height=left_height)
    dpg.set_item_width(item="NodeExplorerWindow",width=left_width)
    dpg.set_item_pos(item="NodeExplorerWindow",pos=explorer_coord)
    dpg.set_item_height(item="NodeEditorWindow",height=right_height)
    dpg.set_item_width(item="NodeEditorWindow",width=right_width)
    dpg.set_item_pos(item="NodeEditorWindow",pos=editor_coord)

def setup_main_window():
    dpg.set_viewport_resize_callback(on_viewport_resize)
    
    # Create graph and node editor
    graph = NodeGraph()
    editor = NodeEditor(graph)
    editor.create()

    # Create Node Explorer
    reg=NodeRegistry()
    reg.discover()
    explorer = NodeExplorer(registry=reg)
    explorer.create()

    # Create Properties Window
    with dpg.window(label="Properties", tag="PropertiesWindow"):
        pass

    dpg.maximize_viewport()
    