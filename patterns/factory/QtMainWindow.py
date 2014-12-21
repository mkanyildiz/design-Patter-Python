from factory.Window import Window

__author__ = 'Muhammed5'

class QtMainWindow(Window):
    def __init__(self):
        Window.__init__(self, "Qt", "MainWindow")