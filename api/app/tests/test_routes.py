import time
import json
from datetime import datetime, timedelta


def test_create_product(client) -> None:
    """
    Test 1: An missing json body should trigger an error
    Test 2: A right JSON should create the product
    Test 3: Test delete end_point
    """
    # Test 1
    resp = client.post("/product")
    assert resp.status_code == 400
    # Test 2
    resp = client.post("/product", json={"price": 10, "name": "Cool Product!"})
    assert resp.status_code == 200
    # Test 3
    resp = client.delete("/product/1")
    assert resp.status_code == 200


def test_document_at(client) -> None:
    """
    Test 1: Make sure that three products are in the database
    Test 2: Update price in Product#2
    Test 3: Get info in Product#2 and ensure that the value is updated
    """
    # Creating three products
    client.post("/product", json={"price": 10, "name": "Product #1"})
    client.post("/product", json={"price": 20, "name": "Product #2"})
    client.post("/product", json={"price": 30, "name": "Product #3"})
    # Test 1
    resp = client.get("/products")
    assert resp.status_code == 200
    assert len(json.loads(resp.data)["products"]) == 3
    # Test 2
    resp = client.put("/product/2", json={"name": "NewProduct#2", "price": 25})
    assert resp.status_code == 200
    # Test 3
    resp = client.get("/product/2")
    assert resp.status_code == 200
    assert json.loads(resp.data)["name"] == "NewProduct#2"
    assert json.loads(resp.data)["price"] == 25
