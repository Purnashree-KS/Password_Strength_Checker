# Password Strength Checker

A Flask-based web application that validates user inputs (**username, email, and password**) using regex rules. The application ensures that all fields follow predefined validation requirements, and users cannot proceed until the inputs are valid.

## Features

* Validates **username, email, and password** using regex.
* Prevents submission until all inputs meet the rules.
* Built with **Python (Flask), HTML, and CSS**.
* Focused on **secure and structured input handling**.

## Input Rules

* **Username**: Only letters, numbers, dots, and underscores allowed.
* **Email**: Must follow standard email format (example: [name@example.com](mailto:name@example.com)).
* **Password**:

  * Minimum length: 8 characters
  * Must include at least one uppercase letter
  * Must include at least one lowercase letter
  * Must include at least one number
  * Must include at least one special character (!, @, #, \$, %, &, \*)

## Project Structure

```
Password-Strength-Checker/
│
├── app.py              # Flask application (main backend file)
├── templates/
│   └── index.html      # HTML frontend
├── static/
│   └── styles.css      # CSS styling
└── README.md           # Project documentation
```

## Installation

1. Install Python on your system (version 3 recommended).
2. Install Flask using pip.
   Example: pip install flask
3. Clone or download this repository.
4. Place all files (Python, HTML, CSS) in one project folder.

## Usage

1. Open the project folder.
2. Run the Flask application file (e.g., app.py).
3. Open a web browser and go to:
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
4. Enter a username, email, and password.
5. The form will only submit once all fields meet the validation rules.

## Learning Outcome

* Used **Flask** for backend development.
* Applied **regex** for input validation.
* Learned basics of **form handling and security** in web applications.
