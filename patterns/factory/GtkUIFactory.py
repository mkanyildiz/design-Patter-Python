from patterns.factory.GtkLayersWindow import GtkLayersWindow
from patterns.factory.GtkMainWindow import GtkMainWindow
from patterns.factory.GtkToolboxWindow import GtkToolboxWindow
from patterns.factory.UIFactory import UIFactory

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