

from flask import Flask, request, jsonify
from order.py import Order

app = Flask(__name__)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    component_codes = data.get('components')

    if not component_codes:
        return jsonify({'error': 'Components are required'}), 400

    order = Order(component_codes)

    if not order.is_valid():
        return jsonify({'error': 'Invalid order'}), 400

    order.calculate_total()
    return jsonify(order.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)
