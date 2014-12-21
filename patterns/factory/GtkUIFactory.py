from factory.GtkLayersWindow import GtkLayersWindow
from factory.GtkMainWindow import GtkMainWindow
from factory.GtkToolboxWindow import GtkToolboxWindow
from factory.UIFactory import UIFactory

__author__ = 'Muhammed5'
class GtkUIFactory(UIFactory):
    def getToolboxWindow(self):
        return GtkToolboxWindow()

    def getLayersWindow(self):
        return GtkLayersWindow()

    def getMainWindow(self):
        return GtkMainWindow()