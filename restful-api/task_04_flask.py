#!/usr/bin/python3

from flask import Flask, jsonify, request

# Instantiate a Flask web
app = Flask(__name__)

# dictionary store user data
users = {}


# route for the root URL ("/")
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Create a new route /data
@app.route('/data')
def get_data():
    return jsonify(list(users.keys()))


# Add a route to return OK status
@app.route('/status')
def get_status():
    return "OK"


# route to get user information username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


# route to POST requests, add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    new_user = request.json
    username = new_user.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {
        "username": username,
        "name": new_user.get('name'),
        "age": new_user.get('age'),
        "city": new_user.get('city')
    }
    return jsonify({"message": "User added", "user": users[username]}), 200


# Run the Flask development server
if __name__ == "__main__":
    app.run(port=5000)
