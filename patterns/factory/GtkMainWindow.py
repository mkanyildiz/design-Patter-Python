from patterns.factory.Window import Window

__author__ = 'Muhammed5'

class GtkMainWindow(Window):
    """
    GtkMainWindow
    :param Window: reference of the class Window
    """
    def __init__(self):
        """

        :return: nothing
        """
        Window.__init__(self, "Gtk", "MainWindow")