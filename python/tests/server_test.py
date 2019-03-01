import unittest
from python.src.server import Server


class ServerTest(unittest.TestCase):

    def test_something(self):
        s = Server()
        self.assertEqual(42, s.what_is_the_answer())


if __name__ == '__main__':
    unittest.main()
