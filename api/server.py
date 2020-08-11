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


@app.route("/data")
def data_view():
    return {
        "corona_dead": [{"date": "11/06/2020", "count": 10},
                        {"date": "12/06/2020", "count": 11}]
    }


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1")
