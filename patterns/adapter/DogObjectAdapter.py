class DogAdapter(object):
    """
    DogAdapter
    :param object:recieving object from main class
    """
    """Adapts the Dog class through encapsulation"""
    def __init__(self, canine):
        """

        :param canine: parsing object
        :return: nothing
        """
        self.canine = canine

    def make_noise(self):
        """

        :return: value of method
        """
        """This is the only method that's adapted"""
        return self.canine.bark()

    def __getattr__(self, attr):
        """

        :param attr: attribute
        :return getattr: cannine
        """
        """Everything else is delegated to the object"""
        return getattr(self.canine, attr)