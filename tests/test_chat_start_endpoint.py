import requests

def test_chat_start_endpoint():
    # Replace 'your-auth-token' and 'receiver-username' with valid values
    auth_token = 'your-auth-token'
    receiver_username = 'receiver-username'
    headers = {'Authorization': f'Token {auth_token}'}
    data = {'receiver': receiver_username}

    url = 'http://127.0.0.1:8000/api/chat/start/'
    response = requests.post(url, headers=headers, data=data)

    assert response.status_code == 200  # Check for a successful request (status code 200)
    response_data = response.json()

    # Assertions for the response data
    assert 'status' in response_data
    assert 'message' in response_data
    assert 'sender' in response_data
    assert 'receiver' in response_data

    # Add more assertions as needed

if __name__ == '__main__':
    test_chat_start_endpoint()
