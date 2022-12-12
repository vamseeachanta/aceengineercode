# Example to utilize pytest
import unittest


def hello_world():
    # pass
    return('hello world')

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    # pass
    return const * (x) ** power


class TestExample2(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), 'hello world')

    def test_custom_num_list(self):
        self.assertEqual(len(create_num_list(10)), 10)

    def test_custom_func_x(self):
        self.assertEqual(custom_func_x(3, 2, 3), 54)


if __name__ == "__main__":
    print("Executing 3 example unittests")
    unittest.main()
