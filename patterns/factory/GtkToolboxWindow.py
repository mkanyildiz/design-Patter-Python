from factory.Window import Window

__author__ = 'Muhammed5'

class GtkToolboxWindow(Window):
    def __init__(self):
        Window.__init__(self, "Gtk", "ToolboxWindow")