from flask import Flask

app = Flask(__name__)


@app.route('/inicio')
def hello_world():
    return '<h1>Hello world!</h1>'


app.run()
