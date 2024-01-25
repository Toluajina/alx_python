from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 7-db_setup.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

############################# TO DO 1 ############################
# Configure Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
###############################################################

db = SQLAlchemy(app)

############################  TO DO 2 ##############################
# Define the User Model class here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
#################################################################

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables

@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
