from factory.QtLayersWindow import QtLayersWindow
from factory.QtMainWindow import QtMainWindow
from factory.QtToolboxWindow import QtToolboxWindow
from factory.UIFactory import UIFactory

__author__ = 'Muhammed5'
class QtUIFactory(UIFactory):
    def getToolboxWindow(self):
        return QtToolboxWindow()

    def getLayersWindow(self):
        return QtLayersWindow()

    def getMainWindow(self):
        return QtMainWindow()