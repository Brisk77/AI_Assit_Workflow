from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Basic email validation regex
EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update-settings', methods=['POST'])
def update_settings():
    data = request.get_json() or {}
    errors = {}

    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    age = data.get('age')

    # Username Validation
    if not username:
        errors['username'] = 'Username is required.'
    elif len(username) < 3 or len(username) > 20:
        errors['username'] = 'Username must be between 3 and 20 characters.'

    # Email Validation
    if not email:
        errors['email'] = 'Email address is required.'
    elif not re.match(EMAIL_REGEX, email):
        errors['email'] = 'Please enter a valid email address.'

    # Age Boundary Checks
    if age is None or str(age).strip() == '':
        errors['age'] = 'Age is required.'
    else:
        try:
            age_num = int(age)
            if age_num < 18 or age_num > 120:
                errors['age'] = 'Age must be between 18 and 120.'
        except ValueError:
            errors['age'] = 'Age must be a valid integer.'

    if errors:
        return jsonify({'errors': errors}), 400

    return jsonify({'status': 'saved', 'message': 'Profile settings updated successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)