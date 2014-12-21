__author__ = 'Muhammed5'
class Window:
    __toolkit = ""
    __purpose = ""

    def __init__(self, toolkit, purpose):
        self.__toolkit = toolkit
        self.__purpose = purpose

    def getToolkit(self):
        return self.__toolkit

    def getType(self):
        return self.__purpose