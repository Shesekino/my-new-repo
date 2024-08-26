const express = require('express');
const app = express();

app.get('/cause-error', (req, res) => {
    throw new Error('Something went wrong!');
});

app.listen(3001, () => {
    console.log('Server is running on http://localhost:3001');
});
