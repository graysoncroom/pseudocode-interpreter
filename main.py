from sys import argv
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return 'Index Page'

if __name__ == '__main__':
    app.run()