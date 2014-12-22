from adapter.Dog import Dog
from adapter.DogObjectAdapter import DogAdapter
from adapter.Person import Person

__author__ = 'Muhammed5'
class mainclass:
    """
    mainclass
    """
    def exercise_system(self):
        person = Person("Bob")
        canine = DogAdapter(Dog("Fido"))

        for critter in (person, canine):

            print(critter.name, "says", critter.make_noise())

if __name__ == "__main__":
    mainclass.exercise_system()