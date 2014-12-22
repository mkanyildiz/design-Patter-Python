from patterns.factory.Window import Window

__author__ = 'Muhammed5'

class GtkToolboxWindow(Window):
    """
    GtkToolboxWindow
    :param Window: reference of the class Window
    """
    def __init__(self):
        """

        

        :rtype : object
        """
        Window.__init__(self, "Gtk", "ToolboxWindow")