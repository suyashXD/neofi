import requests

def test_suggested_friends_endpoint():
    # Replace 'your-auth-token' and 'your-user-id' with valid values
    auth_token = 'your-auth-token'
    user_id = 'your-user-id'
    headers = {'Authorization': f'Token {auth_token}'}

    url = f'http://127.0.0.1:8000/api/suggested-friends/{user_id}/'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200  # Check for a successful request (status code 200)
    response_data = response.json()

    # Assertions for the response data
    assert 'suggested_friends' in response_data
    suggested_friends = response_data['suggested_friends']

    # You can add more assertions to validate the structure of the suggested_friends data

if __name__ == '__main__':
    test_suggested_friends_endpoint()
