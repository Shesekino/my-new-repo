const express = require('express');
const app = express();

// Simulated route that throws an error
app.get('/cause-error', (req, res) => {
    throw new Error('Something went wrong!');
});

// Custom error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack); // Log the error stack trace internally
    res.status(500).json({ error: 'An unexpected error occurred. Please try again later.' }); // Send generic error message
});

app.listen(3001, () => {
    console.log('Server is running on http://localhost:3001');
});
