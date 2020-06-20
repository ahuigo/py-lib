from flask import Flask
import time
import random
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get('http://localhost:8082/ping')
    print("hello", random.random(), r.text)
    return 'Hello, World!'

app.run(port=5000, threaded=True)
