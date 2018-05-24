def my_decorator(some_function):

    def wrapper():

        num = 10

        if num == 10:
            print("Yes!")
        else:
            print("No!")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


# if __name__ == '__main__':
#     my_decorator()

@my_decorator
def just_some_function():
    print("Whee!")

just_some_function()
