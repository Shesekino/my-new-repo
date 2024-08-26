const http = require('http')
const validAdminToken = "valid_admin_token";

const server = http.createServer((req, res) => {
    if (req.url === '/admin') {
        const authHeader = req.headers['authorization'];
        if (authHeader === `Bearer ${validAdminToken}`) {
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end('Welcome to the admin page!');
        } else {
            res.writeHead(403, { 'Content-Type': 'text/plain' });
            res.end('Access denied.');
        }
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Page not found.');
    }
});

server.listen(8000, () => {
    console.log('Serving on port 8000');
});
