from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import half_time_lib
import activity_decay_function as activity_func

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes and origins

@app.route('/calculate', methods=['POST', 'OPTIONS'])
def calculate():
    if request.method == 'OPTIONS':
        response = app.make_response('')
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    data = request.json
    isotope = data.get('element')
    start_date_str = data.get('start')
    end_date_str = data.get('end')
    initial_activity = float(data.get('initialActivity'))  # Convert to float

    half_life = half_time_lib.get_half_life(isotope)
    if half_life is None:
        return jsonify({"error": "Isotope not found"}), 404

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    t = (end_date - start_date).total_seconds() / (365.25 * 24 * 3600)  # Convert seconds to years

    current_activity = activity_func.calculate_activity(initial_activity, t, half_life)
    response = jsonify({"current_activity": float(current_activity)})  # Convert to native Python float
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



@app.route('/data', methods=['GET'])
def get_half_life_data():
    half_life_data = half_time_lib.get_all_half_life_data()
    return jsonify(half_life_data)

if __name__ == '__main__':
    app.run(debug=True)