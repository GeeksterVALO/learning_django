from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])    
def hello():
    if request.method == 'POST': 
        return "Hello, POST!"
    return "Hello, GET!"