import unittest


class TestedClass:
    def act(self):
        raise Exception("raising exception!")


class TestMath(unittest.TestCase):

    def test_raises_exception(self):
        testedObject = TestedClass()
        self.assertRaises(Exception, testedObject.act)
#        with self.assertRaises(Exception):
#            testedObject.act()

if __name__ == '__main__':
    unittest.main()

