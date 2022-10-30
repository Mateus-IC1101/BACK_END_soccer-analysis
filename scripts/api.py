from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def root():
    return '<p>xxxxx</p>'


@app.route('/users', methods=['GET'])
def summary():
    return usersAll()


def usersAll():
    users = [
        {
            'nome': 'mateus',
            'idade': 23
        },
        {
            'nome': 'marcos',
            'idade': 26
        }
    ]

    return users
