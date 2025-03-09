import requests

BASE_URL = "http://127.0.0.1:5000/api/products"

def test_get_products():
    response = requests.get(BASE_URL)
    assert response.status_code == 200