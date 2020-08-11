from flask import Flask

app = Flask(__name__)


@app.route('/')  # I'm a route
def hello_world():
    return 'Hello, World!'


@app.route('/corona')
def corona_view():
    return "Over 600 death in Israel currently"


@app.route("/greet/<string:name>")
def greet_view(name: str):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1")
