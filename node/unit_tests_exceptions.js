const assert = require('node:assert');
const test = require('node:test');

function buggyFunction() {
  throw new Error('oops!');
}

test('catching an error!', (t) => {
  assert.throws(buggyFunction, Error);
});

