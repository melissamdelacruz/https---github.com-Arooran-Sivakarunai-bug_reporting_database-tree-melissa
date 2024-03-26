from flask import Flask, request, render_template
from flask_mail import *
import re

def passreqs(password):
    # Check for at least one uppercase letter
    uppercase_regex = re.compile(r'[A-Z]')
    if not uppercase_regex.search(password):
        return False

    # Check for at least one lowercase letter
    lowercase_regex = re.compile(r'[a-z]')
    if not lowercase_regex.search(password):
        return False

    # Check for at least one special character
    special_char_regex = re.compile(r'[^A-Za-z0-9]')
    if not special_char_regex.search(password):
        return False

    # All requirements met
    return True

def update_password(new_password, conf_password):
    if new_password != conf_password:
        return "Error: Ensure Passwords are Identical!"
    
    if not passreqs(new_password):
        return "Error: Password does not meet requirements!"

    # Perform password update here (not implemented in this example)
    return "Password Updated!"

def create_app():
    app = Flask(__name__)

    @app.route("/", methods=['GET', 'POST'])
    def index():
        return render_template("update_password.html")
    
    @app.route("/update_password", methods=["POST"])
    def handle_update_password():
        new_password = request.form.get("new_password")
        conf_password = request.form.get("conf_password")
      
        result = update_password(new_password, conf_password)
        return result

    return app

if __name__ == "__main__":
    # Run the app on port 5001
    app = create_app()
    app.run(port=5001)


if __name__ == "__main__":
    # Run the app on port 5001
    app = create_app()
    app.run(port=5001)