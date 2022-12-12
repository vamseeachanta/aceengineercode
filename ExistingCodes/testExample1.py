import unittest


def hello_world():
    # pass
    return('hello world')


class TestExample1(unittest.TestCase):
    def setUp(self):
        pass

    def test_hello_world(self):
        self.assertEqual(hello_world(), 'hello world')

    def tearDown(self):
        pass

if __name__ == "__main__":
    print("Executing 1 example unittest")
    unittest.main()
