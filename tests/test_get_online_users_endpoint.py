import requests

def test_get_online_users_endpoint():
    # Replace 'your-auth-token' with a valid authentication token
    auth_token = 'your-auth-token'
    headers = {'Authorization': f'Token {auth_token}'}

    url = 'http://127.0.0.1:8000/api/get-online-users/'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200  # Check for a successful request (status code 200)
    response_data = response.json()

    # Assertions for the response data
    assert isinstance(response_data, list)  # Assuming the response is a list of online users

    # Add more assertions as needed

if __name__ == '__main__':
    test_get_online_users_endpoint()
