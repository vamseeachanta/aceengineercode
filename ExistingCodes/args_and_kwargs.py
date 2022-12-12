def print_kwargs(*args, **kwargs):
    '''
    Limitation: Only works from 1 python program to another
    Limitation: The same key words become strings delimited by space when entered from dos window as system arguments
    '''

    print("Printing: kwargs, Length of kwargs is : {0}" .format(len(kwargs)))
    print(kwargs)
    for key, value in kwargs.items():
        print("The value of {0} is {1}".format(key, value))

    print("Printing: args, Length of args is : {0}" .format(len(args)))
    for arg in args:
        print(arg)



if __name__ == "__main__":
    print("=========================================================")
    print("\nSending a dictionary does not work as kwarg. It works as an agrument")
    print_kwargs(303, {'kwargs_1':"Shark", 'kwargs_2':4.5, 'kwargs_3':True})

    print("=========================================================")
    print("\nSending both args and kwargs")
    print("\nkeyword = value format works as kwargs")
    print_kwargs(303, kwargs_1 = "Shark", kwargs_2 = 4.5, kwargs_3 = True)

    print("=========================================================")
    print("\nSend only argument")
    print_kwargs(303)

    print("=========================================================")
    print("\nSend only kwargs")
    print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
