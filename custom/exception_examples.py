class ExceptionExamples():

    def __init__(self):
        pass

    def generate_error(self):
        for i in range(5):
            if i == 3:
                raise ValueError('Raising Value Error is Successful!')
            print(f'i = {i}')

    def check_exceptions(self):
        try:
            print('Inside of try...')
            self.generate_error()
            # raise ValueError('This is a value error!')
        except Exception as ex:
            print(f'Caught exception as Value Error: {ex}')
        # except ValueError:
        #     print('Caught exception')


if __name__ == '__main__':
    exception_examples = ExceptionExamples()
    exception_examples.check_exceptions()
