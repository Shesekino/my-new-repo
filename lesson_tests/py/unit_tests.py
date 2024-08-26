import unittest


class TestMath(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(5, 2 + 2)


if __name__ == '__main__':
    unittest.main()

