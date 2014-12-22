

class Person(object):
    """
    Person
    :param object: reference from main class
    """
    """A representation of a person in 2D Land"""
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        """
        :return String value
        """
        return "hello"