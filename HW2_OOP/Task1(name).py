class Animal:

    def eat(self):
        print(f'{self.__class__.__name__} is eating')

    def sleep(self):
        print(f'{self.__class__.__name__} is sleeping')

class Dog(Animal):
    def bark(self):
        print(f'{__class__.__name__} is barking')

class Horse(Animal):
    def run(self):
        print(f'{__class__.__name__} is running')

class Cat(Animal):
    def catch(self):
        print(f'{__class__.__name__} is catching mice')

class Lion(Animal):
    def hunt(self):
        print(f'{__class__.__name__} is hunting')

class Bird(Animal):
    def fly(self):
        print(f'{__class__.__name__} is flying')

dog = Dog()
horse = Horse()
cat = Cat()
lion = Lion()
bird = Bird()

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
      f'{isinstance(cat, Animal)},'
      f'{isinstance(horse, Animal)},'
      f'{isinstance(lion, Animal)},'
      f'{isinstance(bird, Animal)}')
