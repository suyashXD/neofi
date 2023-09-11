import requests

def test_chat_send_endpoint():
    # Replace 'your-auth-token', 'receiver-username', and 'your-message' with valid values
    auth_token = 'your-auth-token'
    receiver_username = 'receiver-username'
    message = 'your-message'
    headers = {'Authorization': f'Token {auth_token}'}
    data = {'receiver': receiver_username, 'message': message}

    url = 'http://127.0.0.1:8000/api/chat/send/'
    response = requests.post(url, headers=headers, data=data)

    assert response.status_code == 200  # Check for a successful request (status code 200)
    response_data = response.json()

    # Assertions for the response data
    assert 'status' in response_data
    assert 'message' in response_data

    # Add more assertions as needed

if __name__ == '__main__':
    test_chat_send_endpoint()
