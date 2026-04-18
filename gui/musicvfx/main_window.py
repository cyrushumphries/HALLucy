import dearpygui.dearpygui as dpg
from musicvfx.graph.node_graph import NodeGraph
from musicvfx.widgets.node_editor import NodeEditor
from musicvfx.nodes.audio.oscillator import Oscillator

def setup_main_window():
    dpg.create_context()
    dpg.create_viewport(title="MusicVFX", width=1600, height=900)

    with dpg.window(label="DockSpace", tag="DockSpace", no_title_bar=True, no_close=True):
        dpg.add_text("Main Dockspace")
        dpg.add_spacer(height=5)
        dpg.add_separator()

    with dpg.window(label="3D Preview"):
        dpg.add_text("OpenGL preview will go here")

    with dpg.window(label="Inspector"):
        dpg.add_text("Block parameters will appear here")

    with dpg.window(label="Audio Analyzer"):
        dpg.add_text("FFT, beat detection, etc.")
        
    # # Create the node editor
    graph = NodeGraph()
    editor = NodeEditor(graph)
    editor.create()
    
    node1 = graph.add_node(Oscillator)
    node2 = graph.add_node(Oscillator)
    node3 = graph.add_node(Oscillator)
    editor.draw_node(node1)    
    editor.draw_node(node2)
    editor.draw_node(node3)

    dpg.setup_dearpygui()
    dpg.show_viewport()

