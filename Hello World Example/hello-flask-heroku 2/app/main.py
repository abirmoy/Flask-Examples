#https://dev.to/techparida/how-to-deploy-a-flask-app-on-heroku-heb

from flask import Flask
app= Flask(__name__)
@app.route('/')
def index():
  return "<h1>Welcome to CodingX</h1>"