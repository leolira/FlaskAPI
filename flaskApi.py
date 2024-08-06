from flask import Flask, jsonify, request
import json

users = [
    {'id': 1, 'name':'Leonardo', 'lastname': 'Amorim', 'age': 42 },
    {'id': 2, 'name': 'Luana', 'lastname': 'Menezes', 'age': 35}
]

def id_generator():
    return max(users['id'] for user in users)+1


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the users list!'})

# List endpoint
@app.route('/users')
def get_users():
    return jsonify({'users':users})

# Specific user endpoint
@app.route('/users/<int:id>', methods = ['GET'])
def get_user_byId(id):
    user = next((user for user in users if user['id'] == id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message':'User not found'}), 404

# Create user endpoint
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = id_generator()
    users.append(new_user), 201
    return jsonify(new_user, {'message':'User created successfully!'})

# Update user endpoint
@app.route('/users', methods=['PUT'])
def update_user():
    user = next((user for user in users if user['id'] == id), None)
    if user:
        user.update(request.get_json())
        return jsonify(user)
    else:
        return jsonify({'message':'User not found'}), 404
    
# Delete user endpoint
@app.route('/users', methods=['DELETE'])
def delete_user():
    user = next ((user for user in users if user['id'] == id), None)
    if user:
        users.remove(user)
        return jsonify({'message': 'User {user.name} removed successfully!'})
    else:
        return jsonify({'message': 'User not found!'}), 404
    
if __name__  == '__main__':
    app.run(debug=True)