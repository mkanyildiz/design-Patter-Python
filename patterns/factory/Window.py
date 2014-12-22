__author__ = 'Muhammed5'
class Window:
    """
    Window
    """
    __toolkit = ""
    __purpose = ""

    def __init__(self, toolkit, purpose):
        """

        :param toolkit:
        :param purpose:
        :return:
        """
        self.__toolkit = toolkit
        self.__purpose = purpose

    def getToolkit(self):
        """
        :return: toolkit
        """
        return self.__toolkit

    def getType(self):
        """
        :return: __purpose
        """
        return self.__purpose