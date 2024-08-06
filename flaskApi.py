from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

if __name__  == '__main__':
    app.run()

@app.route('/users')
def get_users():
    users = ['User 01', 'User 02']
    return jsonify({'users':users})

