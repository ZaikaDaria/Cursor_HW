from abc import ABC, abstractmethod
import random


class Human(ABC):

    @abstractmethod
    def info(self):
        raise NotImplementedError

    @abstractmethod
    def make_money(self, income):
        raise NotImplementedError

    @abstractmethod
    def buy_house(self, house):
        raise NotImplementedError


class House:
    def __init__(self, cost, area):
        self.area = area
        self.cost = cost


class SmallHouse(House):
    def __init__(self, cost, area=40):
        super().__init__(cost, area)


class Person(Human):
    def __init__(self, name, age, wealth, own_property=[]):
        self.name = name
        self.age = age
        self.wealth = wealth
        self.own_property = own_property

    def info(self):
        print(f'Name: {self.name}'+'\n'
              f'Age: {self.age}'+'\n'
              f'Budget: {self.wealth}'+'\n'
              f'Own propery: {self.own_property}')

    def make_money(self, income):
        self.wealth += income
        print(f'Available budget after income is {self.wealth}')

    def buy_house(self, house, discount):
        if self.wealth >= house.cost:
            self.wealth -= int(house.cost - (house.cost * discount))
            self.own_property.append(house)
        print(f'{self.name} just bought the {str(house)}. Current budget is {self.wealth}')


class RealtorUnique(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorUnique):
    def __init__(self, name, discount, obj_list=[]):
        self.name = name
        self.discount = float(discount)
        self.obj_list = obj_list

    def info(self):
        print(f'Realtor {self.name} can offer to sold the next {self.obj_list}')

    @staticmethod
    def stealing(person):
        stolen = round(float(person.wealth * random.uniform(0, 0.10)), 2)
        person.wealth -= stolen
        return f'Realtor stole {stolen} amount of money. Currently {person.name} has {person.wealth}'

    def discount(self):
        return self.discount

    def sold(self, house):
        if Person.buy_house(house):
            self.obj_list.remove(house)
            print(f'{self.name} just sold the {str(house)}')


annrealtor = Realtor('Anna', 0.1, ['house1', 'house2', 'house3'])
person = Person("Poul", 36, 20000, ['dacha'])
house = House(10000, 30)
print(person.info(), person.buy_house(house, annrealtor.discount))

