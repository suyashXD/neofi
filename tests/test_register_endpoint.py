import requests

def test_register_endpoint():
    url = 'http://127.0.0.1:8000/api/register/'
    data = {
        'username': 'suyashsrivastava',
        'password': '123',
        'email': 'suyashsrivastava@example.com',
        'first_name': 'Suyash',
        'last_name': 'Srivastava',
    }
    response = requests.post(url, data=data)

    assert response.status_code == 201  # Check for a successful registration (status code 201)
    response_data = response.json()
    
    # Assertions for the response data
    assert 'token' in response_data
    assert 'user_info' in response_data
    assert response_data['user_info']['username'] == 'suyashsrivastava'
    assert response_data['user_info']['email'] == 'suyashsrivastava@example.com'
    assert response_data['user_info']['first_name'] == 'Suyash'
    assert response_data['user_info']['last_name'] == 'Srivastava'

    # Add more assertions as needed

if __name__ == '__main__':
    test_register_endpoint()
