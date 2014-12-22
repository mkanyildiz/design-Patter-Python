class DogAdapter(object):
    """Adapts the Dog class through encapsulation"""
    def __init__(self, canine):
        self.canine = canine

    def make_noise(self):
        """This is the only method that's adapted"""
        return self.canine.bark()

    def __getattr__(self, attr):
        """Everything else is delegated to the object"""
        return getattr(self.canine, attr)