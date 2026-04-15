import dearpygui.dearpygui as dpg
from musicvfx.main_window import setup_main_window

def main():
    setup_main_window()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    main()

