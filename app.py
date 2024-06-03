from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloworld():
    return "<h1>hello jenkins</h1>"