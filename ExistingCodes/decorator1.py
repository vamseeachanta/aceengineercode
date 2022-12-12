import functools


def my_decorator(mainFunction):
	@functools.wraps(mainFunction)
	def function_that_runs_mainFunction():
		print("I am the decorator function")
		mainFunction()
		print("End of decorator function")
	return function_that_runs_mainFunction

@my_decorator
def mainFunction():
	print("I am the main function running inside the decorator")

mainFunction()