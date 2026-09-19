# *args — Multiple Arguments
from ast import List
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print(add_numbers(10, 20))
print(add_numbers(10, 20, 30, 40))

# **kwargs — Multiple Keyword Arguments
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
student_details(
    name="Krishna",
    age=22,
    course="Python",
    city="Hyderabad"
)

# Normal approach:
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num * num)
print(squares)

#List comprehension:

numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]
print(squares)

# List Comprehension with Condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squares = {num: num * num for num in numbers}
print(squares)

# map()
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, numbers))
print(result)

# filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)
