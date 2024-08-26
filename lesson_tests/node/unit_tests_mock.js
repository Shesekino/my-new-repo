const assert = require('node:assert');
const { mock, test } = require('node:test');


objectToTest = {
  functionToMock() {
    return [1, 2, 3];
  },
  functionToTest() {
    input = this.functionToMock();
    return input.map((x) => '*' + x + '*');
  },
};

fakeInput = ['a', 'b', 'c'];

test('testing with a mock', (t) => {
  proxy = mock.method(objectToTest, 'functionToMock');
  proxy.mock.mockImplementation(() => {return fakeInput;})
  koko = objectToTest.functionToTest();
  assert.strictEqual(koko[0], '*a*');
});

