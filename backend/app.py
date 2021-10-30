from flask import Flask, jsonify, render_template

from SECRET_KEY import key
from database import db_init

# Init app
app = Flask(__name__)
app.config['SECRET_KEY'] = key

# Setting up connection to the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# init the app
db_init(app)

@app.route('/', methods=["GET"]) # Setting Route
def index():
    return 'Hello World' # Returning msg

if __name__ == "__main__": # checking if the script is being executed or called
    app.run(debug=True) # running the app in debug mode