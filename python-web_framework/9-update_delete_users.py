from flask import Flask, request, render_template, flash
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

############################  TO DO 5 ##############################
# Implement a new route /update_user/<int:user_id> in your flask application
# Ensure this route handles both GET and POST requests.
# For POST requests:
# Extract the updated name and email from the form data.
# Validate the data: ensure both fields are provided.
# Use the given user_id to identify and update the corresponding user in the User table.
# If the update is successful, Flash the message “User updated successfully!”.
# In the case of errors (e.g., invalid user_id, email already taken, etc.), provide a relevant error message.
# For GET requests, render the update_user.html template.
@app.route('/update_user/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        try:
            user.name = name
            user.email = email
            db.session.commit()
            flash("User updated successfully!", 'success')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", 'error')

    return render_template('update_user.html', user=user)

############################  TO DO 6 ##############################
# Establish a new route /delete_user/<int:user_id>.
# On accessing this route, the user with the specified user_id should be removed from the User table.
# After successful deletion, display the message “User deleted successfully!”.
@app.route('/delete_user/<int:user_id>', methods=['GET','POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        try:
            db.session.delete(user)
            db.session.commit()
            flash("User deleted successfully!", 'success')
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {str(e)}", 'error')

    return render_template('delete_user.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
