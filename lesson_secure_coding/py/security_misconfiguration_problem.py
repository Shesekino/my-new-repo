from flask import Flask, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True
users_db = {
    'admin': {'password': 'supersecretpassword',
              'email': 'admin@example.com'},
    'user': {'password': 'userpassword',
             'email': 'user@example.com'}
}

@app.route('/user/<username>')
def get_user(username):
    try:
        user = users_db[username]
        return jsonify(user)
    except KeyError:
        raise ValueError("User not found")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
