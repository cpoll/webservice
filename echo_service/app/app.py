from flask import Flask

app = Flask(__name__)


@app.route('/')
def slash():
    return 'Hi'
