
from p1 import multiple
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(multiple(10), 23, 'Should be 23')


if __name__ == '__main__':
    unittest.main()
