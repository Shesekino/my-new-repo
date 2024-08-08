import unittest
from unittest.mock import Mock


mock = Mock()
def side_effect():
    print("mock.fetch() called!")
    return [1, 2, 3]
mock.fetch = Mock(side_effect=side_effect)


class Tester(unittest.TestCase):

    def test_getList(self):
        testedObject = TestedClass(mock)
        gottenList = testedObject.decorateFetchedList();
        print(gottenList)
        self.assertTrue('*1*' in gottenList)


class TestedClass:
    def __init__(self, fileReader):
        self._fileReader = fileReader

    def decorateFetchedList(self):
        input = self._fileReader.fetch()
        output = []
        for x in input:
            output.append('*' + str(x) + '*')
        return output


if __name__ == '__main__':
    unittest.main()

