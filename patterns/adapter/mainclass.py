from adapter.Dog import Dog
from adapter.DogObjectAdapter import DogAdapter
from adapter.Person import Person

__author__ = 'Muhammed5'
def exercise_system():
    person = Person("Bob")
    canine = DogAdapter(Dog("Fido"))

    for critter in (person, canine):

        print(critter.name, "says", critter.make_noise())

if __name__ == "__main__":
    exercise_system()