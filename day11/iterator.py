# ITERATORS
numbers = [10, 20, 30, 40, 50]
number_iterator = iter(numbers)
print("Using Iterator:")
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
names = [
    "Krishna",
    "Rahul",
    "Arjun"
]
name_iterator = iter(names)
print("\nStudents:")
for name in name_iterator:
    print(name)