# Import Flask and the request object, which handles incoming form data
from flask import Flask, request, render_template
import re

# Create a Flask web server
app = Flask(__name__)

# This function contains your original validation logic
def check_password_strength(username, email, password):
    # Username Validation
    if not re.fullmatch(r'[A-Za-z\.\s]+', username):
        return "Invalid username. Please use only letters, dots, and spaces."

    # Email Validation
    if not re.search(r'^[A-Za-z0-9]+@gmail.com$', email):
        return "Invalid email. Must be a gmail.com address."

    # Password Validation
    if not (7 < len(password) < 20):
        return "Password must be between 8 and 19 characters."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one number."
    if not re.search(r'[!@#$]', password):
        return "Password must contain at least one special character (!, @, #, $)."
    
    # All checks passed
    return "Success! Your username, email, and password are valid."

# This is the main page (e.g., http://127.0.0.1:5000/)
@app.route('/')
def home():
    # Show the login form
    return render_template('login.html')

# This route will handle the form submission
@app.route('/check', methods=['POST'])
def check():
    # Get the data from the form fields
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    # Run your validation logic
    result = check_password_strength(username, email, password)
    
    # Return the result to the user
    return result

# This makes the script runnable
if __name__ == '__main__':
    app.run(debug=True)