from factory.Window import Window

__author__ = 'Muhammed5'

class GtkLayersWindow(Window):
    def __init__(self):
        Window.__init__(self, "Gtk", "LayersWindow")
