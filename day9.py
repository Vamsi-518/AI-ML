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

#Infosys Advanced Python Coding – Next 10 Programs

#1. Longest Substring Without Repeating Characters
s = input("Enter a string: ")

seen = {}
left = 0
max_length = 0
result = ""

for right in range(len(s)):
    char = s[right]

    if char in seen and seen[char] >= left:
        left = seen[char] + 1

    seen[char] = right

    if right - left + 1 > max_length:
        max_length = right - left + 1
        result = s[left:right + 1]

print("Longest Substring:", result)
print("Length:", max_length)


#2. Find All Pairs With Given Sum
arr = list(map(int, input().split()))
target = int(input("Enter target: "))

seen = set()
pairs = set()

for num in arr:
    complement = target - num

    if complement in seen:
        pairs.add(tuple(sorted((num, complement))))

    seen.add(num)

if pairs:
    for pair in sorted(pairs):
        print(pair)
else:
    print("No pairs found")

#3. Rotate an Array by K Positions
arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter rotation: "))

if arr:
    k = k % len(arr)
    rotated = arr[-k:] + arr[:-k] if k else arr
    print("Rotated Array:", rotated)
else:
    print("Empty array")

#4. Merge Two Sorted Arrays Without sort()
a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))

i = 0
j = 0
merged = []

while i < len(a) and j < len(b):

    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged.extend(a[i:])
merged.extend(b[j:])

print("Merged Array:", merged)

#
s = input("Enter a string: ")

result = ""

def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1:right]

for i in range(len(s)):
    odd = expand(i, i)
    even = expand(i, i + 1)

    if len(odd) > len(result):
        result = odd

    if len(even) > len(result):
        result = even

print("Longest Palindrome:", result)


#6. Spiral Traversal of a Matrix
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

top = 0
bottom = rows - 1
left = 0
right = cols - 1

result = []

while top <= bottom and left <= right:

    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print("Spiral Order:", result)


#7. Find Majority Element
arr = list(map(int, input("Enter array: ").split()))

candidate = None
count = 0

for num in arr:
    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

if arr.count(candidate) > len(arr) // 2:
    print("Majority Element:", candidate)
else:
    print("No Majority Element")

#8. Longest Common Subsequence (LCS)
s2 = input("Enter second string: ")

m = len(s1)
n = len(s2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i][j - 1]
            )

print("LCS Length:", dp[m][n])

i, j = m, n
result = []

while i > 0 and j > 0:
    if s1[i - 1] == s2[j - 1]:
        result.append(s1[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print("LCS:", "".join(reversed(result)))

#9. Minimum Number of Coins
coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter amount: "))

if any(c <= 0 for c in coins) or amount < 0:
    print("Invalid input")
else:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        print("Amount cannot be formed")
    else:
        print("Minimum Coins:", dp[amount])

#10. Maximum Product Subarray
arr = list(map(int, input("Enter array: ").split()))

if not arr:
    print("Array is empty")
else:
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    for num in arr[1:]:

        if num < 0:
            max_product, min_product = min_product, max_product

        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)

        result = max(result, max_product)

    print("Maximum Product:", result)