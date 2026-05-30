import dearpygui.dearpygui as dpg
import musicvfx.globals as globals
from musicvfx.main_window import setup_main_window

def main():
    dpg.create_context()
    # dpg doens't report correct viewport sizes when starting maximized or calling 
    # so we need to create a viewport size (taking into account the border size guesstimated values)
    # will be corrected by resize callback in setup_main_window()
    dpg.set_global_font_scale(globals.scale_factor) # Consider the scale factor (important on 4K screens)
    dpg.create_viewport(title="MusicVFX", width=1875, height=1000) 
    dpg.setup_dearpygui()
    dpg.show_viewport(maximized=True)
    
    setup_main_window()

    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()

