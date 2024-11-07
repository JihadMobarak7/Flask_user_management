from flask import Flask, request, jsonify
from flask_cors import CORS
from Database import create_table, get_users, insert_user, get_user_by_id, update_user, delete_user

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the User Management API!"

@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_users())

@app.route('/api/users/add', methods=['POST'])
def api_insert_user():
    user_data = request.get_json()
    return jsonify(insert_user(user_data))

@app.route('/api/users/<int:user_id>', methods=['GET'])
def api_get_user_by_id(user_id):
    return jsonify(get_user_by_id(user_id))

@app.route('/api/users/update', methods=['PUT'])
def api_update_user():
    user_data = request.get_json()
    return jsonify(update_user(user_data))

@app.route('/api/users/delete/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))

if __name__ == '__main__':
    create_table()  # Ensure the table is created upon startup
    app.run(debug=True)