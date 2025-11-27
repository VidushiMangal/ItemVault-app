def my_decorator(my_function):
    def wrapper():
        print("Wrap it in beginning of my function")
        my_function()
        print(f"Wrap it in the end of my_function")
    return wrapper

@my_decorator
def greeting():
    print("Say Hello")
greeting()