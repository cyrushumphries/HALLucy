import dearpygui.dearpygui as dpg
from musicvfx.main_window import setup_main_window

def main():
    dpg.create_context()
    # dpg doens't report correct viewport sizes when starting maximized or calling 
    # so we need to create a viewport size (taking into account the border size guesstimated values)
    # will be corrected by resize callback in setup_main_window()

    dpg.create_viewport(title="MusicVFX", width=1875, height=1000) 
    dpg.setup_dearpygui()
    dpg.show_viewport(maximized=True)
    
    setup_main_window()

    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()

