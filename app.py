from flask import Flask
from flask_sslify import SSLify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"


if __name__ == '__main__':
    app.run(host="localhost", port=5000)