from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__, static_folder='static')

# MongoDB setup
client = MongoClient("mongodb+srv://Harsha1234:Harsha1234@cluster1.nwz3t.mongodb.net/login_db?retryWrites=true&w=majority")
db = client['login_db']
users_collection = db['users']

# Home route
@app.route('/')
def home():
    return render_template('reg.html')  # Ensure `reg.html` exists in the templates folder

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']  # This stores the password in plain text

    # Store data in the MongoDB database
    user = {
        "username": username,
        "password": password  # WARNING: Storing plain text passwords is insecure
    }
    users_collection.insert_one(user)

    return "Login details saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)
