# REST APIs in Python

This presentation was put together for the 2019-02-12 IndyPy meeting Python Beginner's Jam.  

## Slides

[Intro_to_REST_with_Python.pdf](Intro_to_REST_with_Python.pdf) contains the presentation slides for the first portion of the talk.

The code demonstration walks through the code in this repo.  

I will link the YouTube video here when it is released.

## Source Code

Our REST API is allowing maintenance of an IndyPy Meeting resource.

Code for the REST API exists in the [rest_api](rest_api) directory.

[models](rest_api/models) holds the SQLAlchemy model for the meeting in [meeting.py](rest_api/models/meeting.py).

[resources](rest_api/resources) holds the flask_restful Resource that handles the HTTP Verbs for the API in [meeting.py](rest_api/resources/meeting.py)

[db.py](rest_api/db.py) is the simple db object for SQLAlchemy.

[rest_app.py](rest_api/rest_app.py) creates the Flask app for the API.

[run_app.py](run_app.py) will serve the Flask REST API using the built in development server.

[access_api.py](access_api.py) is an client implementation calling the REST API with Requests.

## Setup and Requirements

This code uses f-strings and requires Python 3.6 or higher.  

To install packages needed in your virtual environment, use `pip install -r requirements.txt`

