const http = require('http')

const server = http.createServer((req, res) => {
    if (req.url === '/admin') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Welcome to the admin page!');
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Page not found.');
    }
});

server.listen(8000, () => {
    console.log('Serving on port 8000');
});
