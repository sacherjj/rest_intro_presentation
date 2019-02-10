# REST APIs in Python

This presentation was put together for the 2019-02-12 IndyPy meeting Python Beginner's Jam.  

[Intro to REST with Python.pdf](Intro to REST with Python.pdf) contains the presentation slides for the first portion of the talk.

The code demonstration walks through the code in this repo.  

I will link the YouTube video here when it is released.

Our REST API is allowing maintenace of an IndyPy Meeting resource.

Code for the REST API exists in the `rest_api` directory.

`models` holds the SQLAlchemy model for the meeting.

`resources` holds the flask_restful Resource that handles the HTTP Verbs for the API

`db.py` is the simple db object for SQLAlchemy.

`rest_app.py` creates the Flask app for the API.

[run_app.py](run_app.py) will serve the Flask REST API using the built in development server.

[access_api.py](access_api.py) is an client implementation calling the REST API with Requests.
