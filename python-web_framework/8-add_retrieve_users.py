from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

############################  TO DO 3 ##############################
# Implement a new route /add_user in your Flask application.
# Ensure this route handles both GET and POST requests.
# For POST requests:
# Retrieve name and email from the submitted form data.
# Attempt to insert the new user into the User table of the alx_flask_db database.
# On successful insertion, flash the message “User added successfully!”.
# Handle any exceptions (e.g., duplicate email) by flashing an appropriate error message.
# For GET requests, render the add_user.html template.
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        try:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully!", 'success')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", 'error')

    return render_template('add_user.html')

############################  TO DO 4 ##############################
# Create a new route /users.
# Connect to the alx_flask_db database and retrieve all users from the User table.
# Render the results using an HTML template (recommended file name: 8-users.html).
# Each user should be displayed as: Name: <name>, Email: <email>.
@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
