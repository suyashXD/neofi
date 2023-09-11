import requests

def test_login_endpoint():
    url = 'http://127.0.0.1:8000/api/login/'
    data = {
        'username': 'suyashsrivastava',
        'password': '123',
    }
    response = requests.post(url, data=data)

    assert response.status_code == 200  # Check for a successful login (status code 200)
    response_data = response.json()
    
    # Assertions for the response data
    assert 'token' in response_data
    assert 'user_info' in response_data
    assert response_data['user_info']['username'] == 'suyashsrivastava'
    assert response_data['user_info']['email'] == 'suyashsrivastava@example.com'  # Assuming this is the registered email
    assert response_data['user_info']['first_name'] == 'Suyash'
    assert response_data['user_info']['last_name'] == 'Srivastava'

    # Add more assertions as needed

if __name__ == '__main__':
    test_login_endpoint()
