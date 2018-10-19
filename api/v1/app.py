#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

sales = [
    {
    'id': 1,
    'attendant': 'rick'
},
    {
        'id': 2,
        'attendant': 'morty'
    }
]

products = [
    {
    'id': 1,
    'description': 'sanchezium'
},
    {
        'id': 2,
        'description': 'get_your_shit-together'
    }
]
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.route('/')
def index():
    return "Welcome to Jade Store Management"

@app.route('/store/api/v1/products', methods=['GET'])
def get_products():
    return make_response(jsonify({'products': products}), 200)

@app.route('/store/api/v1/sales', methods=['GET'])
def get_sales():
    return make_response(jsonify({'sales': sales}), 200)

@app.route('/store/api/v1/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = [product for product in products if product['id'] == product_id ]
    if len(product) == 0:
        abort(404)
    return make_response(jsonify({'product': product[0]}), 200)

@app.route('/store/api/v1/sales/<int:sale_id>', methods=['GET'])
def get_sale(sale_id):
    sale = [sale for sale in sales if sale['id'] == sale_id]
    if len(sale) == 0:
       abort(404)
    return make_response(jsonify({'sale': sale[0]}), 200)

@app.route('/store/api/v1/products/', methods=['POST'])
def create_product():
    if not request.json or not 'description' in request.json:
        abort(400)
    product = {
        'id': products[-1]['id'] + 1,
        'description': request.json.get('description',"")
    }

    products.append(product)
    return jsonify({'product': product}), 201

@app.route('/store/api/v1/sales/', methods=['POST'])
def create_sale():
    if not request.json or not 'description' in request.json:
        abort(400)
    sale = {
        'id': sales[-1]['id'] + 1,
        'attendant': request.json.get('attendant',""),
        'description': request.json.get('description', "")
    }

    sales.append(sale)
    return jsonify({'sale': sale}), 201

@app.route('/store/api/v1/sales/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    sale = [sale for sale in sales if sale['id'] == sale_id]
    if len(sale) == 0:
        abort(404)
    if not request.json:
        abort(404)
    if 'attendant' in request.json and type(request.json['attendant']) != unicode:
        abort(404)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(404)
    sale[0]['attendant'] = request.json.get('attendant', sale[0]['attendant'])
    sale[0]['description'] = request.json.get('description', sale[0]['description'])
    return jsonify({'sale': sale}), 201

@app.route('/store/api/v1/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    if not request.json:
        abort(404)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(404)
    product[0]['description'] = request.json.get('description', product[0]['description'])
    return jsonify({'product': product}), 201

@app.route('/store/api/v1/sales/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    sale = [sale for sale in sales if sale['id'] == sale_id]
    if len(sale)  == 0:
        abort(404)
    sales.remove(sale[0])
    return jsonify({'':}), 200

@app.route('/store/api/v1/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = [product for product in products if product['id'] == product_id]
    if len(product) == 0:
        abort(404)
    products.remove(product[0])
    return jsonify({'':}), 200

if __name__ == '__main__':
    app.run(debug=True)