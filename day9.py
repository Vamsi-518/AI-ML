"""
#Encapsulation
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
account = BankAccount("Krishna", 5000)
print(account.name)
print(account.get_balance())
account.deposit(2000)
print(account.get_balance())
"""
"""
# Abstraction

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a button")
car = Car()
bike = Bike()
car.start()
bike.start()
"""
"""
# Polymorphism

class Dog:
    def sound(self):
        print("Dog says Woof")
class Cat:
    def sound(self):
        print("Cat says Meow")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()
"""
"""
# Multiple Inheritance
class Father:
    def skills(self):
        print("Driving")
class Mother:
    def cooking(self):
        print("Cooking")
class Child(Father, Mother):
    pass
child = Child()
child.skills()
child.cooking()
"""
"""
# Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog says Woof")
animal = Animal()
dog = Dog()
animal.sound()
dog.sound()
"""
"""
#super()

class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course
student = Student("Krishna", "Python")
print(student.name)
print(student.course)
"""
"""
# MRO — Method Resolution Order
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("C")
class D(B, C):
    pass
obj = D()
obj.show()
print(D.mro())
"""
"""
# Magic / Dunder Methods
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
student = Student("Krishna", 22)
print(student)
"""
"""
# Dunder __add__
class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
num1 = Number(10)
num2 = Number(20)
print(num1 + num2)
"""