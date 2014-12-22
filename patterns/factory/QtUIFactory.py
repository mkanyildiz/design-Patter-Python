from factory.QtLayersWindow import QtLayersWindow
from factory.QtMainWindow import QtMainWindow
from factory.QtToolboxWindow import QtToolboxWindow
from factory.UIFactory import UIFactory
"""
@author: Kanyildiz
@date: 22.12.2014
"""
class QtUIFactory(UIFactory):
    """
    QtUIFactory
    :param UIFactory: value
    """
    def getToolboxWindow(self):
        """
        :return QtToolboxWindow()
        """
        return QtToolboxWindow()

    def getLayersWindow(self):
        """


        :return QtLayersWindow()
        """
        return QtLayersWindow()

    def getMainWindow(self):
        """


        :return QtMainWindow()
        """
        return QtMainWindow()