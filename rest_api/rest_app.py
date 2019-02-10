from flask import Flask
from flask_restful import Api

from rest_api.resources.meeting import MeetingV1
from rest_api.db import db


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['PROPOGATE_EXCEPTIONS'] = True
app.secret_key = 'indypy_secret'   # This should not be defined in the file and kept secret for a real site


api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(MeetingV1, '/api/v1/meetings', '/api/v1/meetings/<string:meeting_date>')
