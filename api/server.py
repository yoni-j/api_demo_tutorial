from urllib.parse import urljoin

import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')  # I'm a route
def hello_world():
    return 'Hello, World!'


@app.route('/corona')  # I can also be a string
def corona_view():
    return "Over 600 death in Israel currently"


@app.route("/greet/<string:name>")  # I can get params
def greet_view(name: str):
    return f"Hello {name}"


@app.route("/data")
def data_view():
    return {
        "corona_dead": [{"date": "11/06/2020", "count": 10},
                        {"date": "12/06/2020", "count": 11}]
    }


@app.route("/world_clock/<a_timezone>")
def world_clock_view(a_timezone: str):
    base_uri = "http://worldtimeapi.org/api/timezone/"
    normalized_timezone = "/".join(a_timezone.split('.'))
    res = requests.get(urljoin(base_uri, normalized_timezone))
    current_time = res.json().get('datetime')
    return f"in {a_timezone} it's currently {current_time}"


if __name__ == "__main__":
    app.run(port=5000, host="127.0.0.1")
