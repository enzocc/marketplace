import json
from datetime import datetime
from flask import jsonify
from flask import (
    Flask, Response, request
)
from app.core.config import settings
from app.core.database import db
from app.models import Products


def create_app():
    app = Flask("Api")
    app.config.from_object(settings)

    @app.route('/products', methods=["GET"])
    def get_products():
        """
        Instructions:
        GET /products
        A list of products, names, and prices in JSON.
        """
        prods = Products.query.all()
        resp = []
        for prod in prods:
            resp.append({
                "code" : prod.product_code,
                "name" : prod.name,
                "prince" : prod.price
            })
        resp = {"products": resp}
        return Response(json.dumps(resp), status=200, mimetype='application/json')

    @app.route('/product', methods=["POST"])
    def create_product():
        """
        Instructions:
        POST /product
        Create a new product from a JSON body.
        """
        request_data = request.get_json(force=True)
        if not request_data:
            return Response("Missing JSON body\n", status=400)
        product_name = request_data.get("name")
        product_price = request_data.get("price")
        if not (product_price or product_name):
            return Response("Product missing name and price\n", status=400)
        new_product = Products(name=product_name, price=product_price)

        db.session.add(new_product)
        try:
            db.session.commit()
        except Exception as error:
            return Response(str(error._message) + "\n", status=400)
        return Response(status=200)

    @app.route('/product/<product_id>', methods=["GET"])
    def get_product(product_id):
        """
        Instructions:
        GET /product/<product_id>
        Return a single product by id in JSON.
        """
        prod = Products.query.filter_by(product_code=product_id).first()
        resp = {}
        if prod:
            resp = {
                "name" : prod.name,
                "price" : prod.price
            }
        return Response(json.dumps(resp), status=200, mimetype='application/json')

    @app.route('/product/<product_id>', methods=["PUT"])
    def update_product(product_id):
        """
        Instructions:
        PUT /product/<product_id>
        Update a product's name or price by id.
        """
        request_data = request.get_json(force=True)

        if not request_data:
            return Response("Missing JSON body\n", status=400)
        name = request_data.get("name")
        price = request_data.get("price")

        if not (name or price):
            return Response("Request missing name and price\n", status=400)

        prod = Products.query.filter_by(product_code=product_id).first()
        if not prod:
            return Response("Product doesn't exist\n", status=404)
        if price:
            prod.price = price
        if name:
            prod.name = name
        try:
            db.session.commit()
        except Exception as error:
            return Response(str(error._message) + "\n", status=400)
        return Response(status=200)

    @app.route('/product/<product_id>', methods=["DELETE"])
    def delete_product(product_id):
        """
        Instructions:
        DELETE /product/<product_id>
        Delete a product by id.
        """
        prod = Products.query.filter_by(product_code=product_id)
        if not prod:
            return Response("Product doesn't exist\n", status=404)
        prod.delete()
        try:
            db.session.commit()
        except Exception as error:
            return Response(str(error._message) + "\n", status=400)
        return Response(status=200)

    return app
