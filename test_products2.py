import requests

def test_get_all_products():
    '''
    This test should make sure that i am able
    to fetch the full list of product data
    from MongoDB
    '''
    res = requests.get('http://127.0.0.1:8000/products')
    data = res.json()
    assert "products" in data
    assert len(data["products"]) >= 1
    for product in data["products"]:
        assert "name" in product
    