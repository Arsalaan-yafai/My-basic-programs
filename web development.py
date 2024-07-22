import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Arsalaan yafai786"
@app.route("/arsalaan")
def miya ():
    return "Arsalaan yafai2"
app.run(debug=True )