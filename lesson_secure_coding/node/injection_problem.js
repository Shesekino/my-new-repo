const sqlite3 = require('sqlite3').verbose();

let database = new sqlite3.Database(':memory:');
let userInput = "Bob' OR '1'='1"

function initDb(db) {
  db.run("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)");
  db.run("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')");
  db.run("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')");
  console.log("Database initialized with sample data.");
}

database.serialize(() => {
  initDb(database);
  let query = `SELECT * FROM users WHERE name = '${userInput}'`;
  console.log(`Executing query: ${query}`);
  database.all(query, [], (err, rows) => {
    rows.forEach((row) => {
      console.log(row);
    });
  });
});

database.close();
