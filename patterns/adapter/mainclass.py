from patterns.adapter.Dog import Dog
from patterns.adapter.DogObjectAdapter import DogAdapter
from patterns.adapter.Person import Person

__author__ = 'Muhammed5'
class mainclass:
    """
    mainclass
    """
    if __name__ == "__main__":
        person = Person("Bob")
        canine = DogAdapter(Dog("Fido"))

        for critter in (person, canine):

            print(critter.name, "says", critter.make_noise())

