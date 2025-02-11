import requests

from flask import Flask, jsonify

app = Flask(__name__)


def response_handler(type, message):
    return jsonify({"type": type, "message": message})


@app.route("/<location_code>/forecasts/hourly/latest")
def forecast_hourly_latest(location_code):
    if not location_code:
        return response_handler({"type": "error", "message": "Location code required"})

    print(location_code)
    url = (
        "https://api.weather.bom.gov.au/v1/locations/"
        + location_code
        + "/forecasts/hourly"
    )
    response = requests.get(url)

    if response.status_code == 200:
        report_data = response.json().get("data")

        return jsonify(report_data[-1])
    else:
        return jsonify({"error": "Failed to fetch data"}), 500


@app.route("/<location_code>/forecasts/now")
def forecast_now(location_code):
    if not location_code:
        return response_handler({"type": "error", "message": "Location code required"})

    print(location_code)
    url = (
        "https://api.weather.bom.gov.au/v1/locations/"
        + location_code
        + "/forecasts/daily"
    )
    response = requests.get(url)

    if response.status_code == 200:
        report_data = response.json().get("data")

        return jsonify(report_data[0])
    else:
        return jsonify({"error": "Failed to fetch data"}), 500


if __name__ == "__main__":
    app.run(debug=True)
