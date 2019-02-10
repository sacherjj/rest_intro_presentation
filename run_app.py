from rest_api.rest_app import app, db


db.init_app(app)
app.run(port=5000, debug=True)
