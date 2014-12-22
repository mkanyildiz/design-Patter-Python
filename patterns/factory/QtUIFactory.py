
"""
@author: Kanyildiz
@date: 22.12.2014
"""
from patterns.factory.QtLayersWindow import QtLayersWindow
from patterns.factory.QtMainWindow import QtMainWindow
from patterns.factory.QtToolboxWindow import QtToolboxWindow
from patterns.factory.UIFactory import UIFactory


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