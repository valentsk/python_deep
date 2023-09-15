from animals import *
from typing import Any

class AnimalFabric:

    def __new__(cls, animal_type, *args, **kwargs) -> [Mammal, Bird, Fish, Animal, Any]:
        try:
            animal = super().__new__(animal_type)
            animal.__init__()(*args, **kwargs)
            return animal
        except Exception as exc:
            print(f'{exc.__class__.__name__} {exc}')
            return Animal('Cadaver', 1000)

def main():
    dog = AnimalFabric(Mammal, name = 'Pluto', age = 5, voice = 'Wow', hair = 'Long')
    fish = AnimalFabric(Fish, name = 'Nemo', age = 1, voice = 'Boolbool', color = 'Orange')
    bird = AnimalFabric(Bird, name = 'BaronVoron', age = 100, voice = 'CarCar', color = 'Black')
    undenified = AnimalFabric('Non-type', name = 'Fail', age = 1_000, voice = 'NOO', hair = 'No', color = 'No')

    print(dog.get_info(), '\n')
    print(fish.get_info(), '\n')
    print(bird.get_info(), '\n')
    print(undenified.get_info())

if __name__ == '__main__':
    main()