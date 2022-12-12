import functools


def decorator_with_arguments(number):
    def my_decorator(mainFunction):
        @functools.wraps(mainFunction)
        def function_that_runs_mainFunction(*args, **kwargs):
            print("I am the decorator function.")
            print("Perform further checks with 'number' argument")
            if number == 56:
                print("Not running the function")
            else:
                print("Running the function")
                mainFunction(*args, **kwargs)
            print("End of decorator function")
        return function_that_runs_mainFunction
    return my_decorator

@decorator_with_arguments(55)
def my_function_too(x,y):
	print(x+y)

my_function_too(57, 67)