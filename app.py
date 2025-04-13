from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/weather")
def proxy_weather():
    url = "https://api.weather.com/v2/pws/observations/current"
    params = {
        "stationId": "IENUR7",
        "format": "json",
        "units": "e",
        "apiKey": "604b8fd2df5e4ffa8b8fd2df5eaffa79"
    }

    response = requests.get(url, params=params)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run()
