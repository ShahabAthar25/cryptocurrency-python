from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename
import datetime

from SECRET_KEY import key
from database import db_init, db
from models import transaction

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
    return 'hello world' # Returning msg
    
@app.route('/api/transactions/<currentUser>', methods=["GET"]) # Setting Route
def get_transaction(currentUser):
    all_transactions = transaction.query.filter_by(userName=currentUser).first() # Getting a singular image

    if not all_transactions:
        return jsonify({ "msg": "user not found" }), 404

    return jsonify(all_transactions)
    

if __name__ == "__main__": # checking if the script is being executed or called
    app.run(debug=True) # running the app in debug mode