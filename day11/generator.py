# GENERATOR
def student_numbers():
    for number in range(1, 6):
        yield number
numbers = student_numbers()
print("Generator Output:")
for number in numbers:
    print(number)
def even_numbers(limit):
    for number in range(1, limit + 1):
        if number % 2 == 0:
            yield number
print("\nEven Numbers:")
for number in even_numbers(10):
    print(number)