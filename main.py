import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
# print(basedir)
# This file (main.py) will be renamed as __file__
# You get the directory name from os.path.dirname() --> projectFile
# You get the complete path of the file using the os.path.abspath() --> home/users/example/
# basedir --> home/users/example/projectFile

# Setting up the flask app
app = Flask(__name__)

# Setting up the flask application to the database - SQLite

# Configuration step 1

# Setting up the database location -> it conveys the Flask application where the database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# Configuration step 2

# To disable tracking of modification to the database
# By default, it is set to True and this allows you to track all modifications to the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Setting up the database is complete

# Setting up migration
Migrate(app,db) # Connecting the application to the database

################################################################################################

# Creating first table

# Setup a class
class employee(db.Model):
    # Default table name will be the class name with an 's' at the end
    # To manually overwrite the default table name
    __tablename__ = 'employee_details'
    
    # Creating columns 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    nationality = db.Column(db.Text)
    
    # Setup the __init__ method
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality
    
    # String representation of the database
    def __repr__(self):
        return f"employee {self.name} age is {self.age}".format(self.name, self.age)
