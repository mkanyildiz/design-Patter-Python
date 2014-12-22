from factory.GtkLayersWindow import GtkLayersWindow
from factory.GtkMainWindow import GtkMainWindow
from factory.GtkToolboxWindow import GtkToolboxWindow
from factory.UIFactory import UIFactory

__author__ = 'Muhammed5'
class GtkUIFactory(UIFactory):
    """
    GtkUIFactory
    :param UIFactory: reference of the class UIFactory
    """
    def getToolboxWindow(self):
        """
        :return: GtkToolboxWindow()
        """
        return GtkToolboxWindow()

    def getLayersWindow(self):
        """
        :return:  GtkLayersWindow()
        """
        return GtkLayersWindow()

    def getMainWindow(self):
        """
        :return: GtkMainWindow()
        """
        return GtkMainWindow()