import unittest
from app import add

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        # We expect 2 + 2 to be 4
        self.assertEqual(add(2, 2), 4)

    def test_add_negative_numbers(self):
        # We expect -1 + -1 to be -2
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
