__author__ = 'Muhammed5'
class Dog(object):
    """
    Dog
    :param object: recieving object value from main class
    """
    """A representation of a dog in 2D Land"""
    def __init__(self, name):
        """
        :param name: name of owner
        """
        self.name = name
    def bark(self):
        """
        :return: returning a String
        """
        return "woof"