class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'The {self.__class__.__name__} {self.name} is eating')

    def sleep(self):
        print(f'The {self.__class__.__name__} {self.name} is sleeping')

class Dog(Animal):
    def bark(self):
        print(f'The {__class__.__name__} {self.name} is barking')

class Horse(Animal):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print(f'The {__class__.__name__} {self.name} is running')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def catch(self):
        print(f'The {__class__.__name__} {self.name}  is catching mice')

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def hunt(self):
        print(f'The {__class__.__name__} {self.name}  is hunting')

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f'The {__class__.__name__} {self.name} is flying')

dog = Dog('Ben')
horse = Horse('Ben')
cat = Cat('Ben')
lion = Lion('Ben')
bird = Bird('Ben')

dog.bark()
horse.run()
cat.catch()
lion.hunt()
bird.fly()

dog.eat()
cat.sleep()
horse.eat()
lion.sleep()
bird.eat()

print(f'{isinstance(dog, Animal)},'
      f'{isinstance(horse, Animal)},'
      f'{isinstance(cat, Animal)},'
      f'{isinstance(lion, Animal)},'
      f'{isinstance(bird, Animal)}')


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} {self.age} years old is eating')

    def sleep(self):
        print(f'{self.name} {self.age} years old is sleeping')

    def study(self):
        print(f'{self.name} {self.age} years old is studing')

    def work(self):
        print(f'{self.name} {self.age} years old is working')


class Centaur(Human, Animal):

    def fight(self):
        print(f"Centaur {self.name} {self.age} years old is fighting")

    def sleep(self):
        Human.sleep(self)

centaur = Centaur('Ben', 95)
centaur.eat()
centaur.fight()
centaur.sleep()
centaur.work()
centaur.study()