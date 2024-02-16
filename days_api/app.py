"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime

from flask import Flask, Response, request, jsonify

from date_functions import convert_to_datetime, get_day_of_week_on, get_days_between

app_history = []

app = Flask(__name__)


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })


@app.get("/")
def index():
    """Returns an API welcome messsage."""
    return jsonify({"message": "Welcome to the Days API."})


@app.route("/between", methods=["POST"])
def get_time_between():
    if request.method == "POST":
        data = request.json

        if "first" not in data or "last" not in data:
            return jsonify({"error": "Missing required data."}), 400
        try:
            first = convert_to_datetime(data['first'])
            last = convert_to_datetime(data['last'])
            output = get_days_between(first, last)
            add_to_history(request)
            return jsonify({'days': output}), 200

        except:
            return jsonify({"error": "Unable to convert value to datetime."}), 400


@app.route("/weekday", methods=["POST"])
def get_weekday():
    if request.method == "POST":
        data = request.json
        if "date" not in data:
            return jsonify({"error": "Missing required data."}), 400
    try:
        day_dt = convert_to_datetime(data["date"])
        day = get_day_of_week_on(day_dt)
        add_to_history(request)
        return jsonify({"weekday": day}), 200
    except:
        return jsonify({"error": "Unable to convert value to datetime."}), 400


@app.route("/history", methods=["GET", "DELETE"])
def get_history():
    if request.method == "GET":
        args = request.args.to_dict()
        number = args.get("number", '5')

        if not number.isdigit() or 0 >= int(number) or int(number) > 20:
            return jsonify({"error": "Number must be an integer between 1 and 20."}), 400

        req_list = []
        if app_history:
            for each in range(0, int(number)):
                req_list.append(app_history[each])
        return jsonify(req_list), 200


if __name__ == "__main__":
    app.run(port=8080, debug=True)
