from flask import Flask, request, jsonify
from flask_cors import CORS


class LimitWebApp:
    def __init__(self, calculator):
        self.app = Flask(__name__)
        CORS(self.app)
        self.calculator = calculator
        self.register_routes()

    def register_routes(self):
        @self.app.route('/calculate', methods=['POST'])
        def handle_calculate():
            try:
                data = request.json
                if not data:
                    return jsonify({"error": "No JSON data provided"}), 400

                expr = data.get('expression')
                var = data.get('variable')
                point = data.get('point')
                direction = data.get('direction', 'both')

                if not all([expr, var, point]):
                    return jsonify({"error": "Missing parameters: expression, variable, and point are required."}), 400

                result = str(self.calculator.calculate(expr, var, point, direction))

                return jsonify({
                    "input": data,
                    "result": result
                })

            except ValueError as ve:
                return jsonify({"error": f"Calculation error: {str(ve)}"}), 400
            except Exception as e:
                return jsonify({"error": f"Internal server error: {str(e)}"}), 500

    def run(self, host='127.0.0.1', port=5000, debug=True):
        print(f"Starting server on http://{host}:{port}")
        self.app.run(host=host, port=port, debug=debug)
