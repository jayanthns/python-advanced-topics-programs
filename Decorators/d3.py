# Class Decorators


class DecoratorClass(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("Call Method Executed Before {}".format(self.original_function.__name__))
        return self.original_function(*args, *kwargs)


@DecoratorClass
def display():
    print('display function ran')

display()
