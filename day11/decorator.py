# DECORATOR
def logger(func):
    def wrapper():
        print("Function started")
        func()
        print("Function completed")
    return wrapper
@logger
def welcome():
    print("Welcome to Python!")
welcome()
def check_age(func):
    def wrapper(age):
        if age >= 18:
            func(age)
        else:
            print("Access denied: Age must be 18 or above.")
    return wrapper
@check_age
def access_system(age):
    print("Access granted.")
print("\nAge Check:")
access_system(22)
access_system(16)