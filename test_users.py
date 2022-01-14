import requests

def test_get_all_users():
    res = requests.get('http://127.0.0.1:8000/users')
    data = res.json()
    assert 'users' in data
    assert data['users']
    for user in data['users']:
        assert 'username' in user
        assert 'name' in user