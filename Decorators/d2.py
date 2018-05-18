# Function Decorators


def decorator_func(original_function):
    def wrapper_func(*args, **kwargs):
        print("WRAPPER EXECUTED BEFORE {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_func


# (@decorator_func) == (display = decorator_func(display))
@decorator_func
def display():
    print('display function ran')


@decorator_func
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Jayanth', 24)
display()
