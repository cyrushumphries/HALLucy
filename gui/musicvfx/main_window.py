import dearpygui.dearpygui as dpg
from musicvfx.widgets.node_editor import NodeEditor


def setup_main_window():
    dpg.create_context()
    dpg.create_viewport(title="pyMusicVFX", width=1600, height=900)

    with dpg.window(label="DockSpace", tag="DockSpace", no_title_bar=True, no_close=True):
        dpg.add_text("Main Dockspace")
        dpg.add_spacer(height=5)
        dpg.add_separator()

    with dpg.window(label="Node Graph"):
        dpg.add_text("Node graph will go here")

    with dpg.window(label="3D Preview"):
        dpg.add_text("OpenGL preview will go here")

    with dpg.window(label="Inspector"):
        dpg.add_text("Block parameters will appear here")

    with dpg.window(label="Audio Analyzer"):
        dpg.add_text("FFT, beat detection, etc.")
        
    # # Create the node editor
    # editor = NodeEditor(graph)
    # editor.create()
    
    # block1 = MathAdd()
    # block2 = MathAdd()
    # block3 = MathAdd()
    # graph.add_block(block1)
    # graph.add_block(block2)
    # graph.add_block(block3)
    # editor.draw_block(block1)    
    # editor.draw_block(block2)
    # editor.draw_block(block3)

    dpg.setup_dearpygui()
    dpg.show_viewport()

