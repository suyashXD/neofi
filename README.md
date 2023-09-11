# CHATAPP

## Description

Chatapp is a chat application created using Django that allows users to create accounts, login, view online users, start chats with online users, and restrict sending messages to offline users.

## Prerequisites

- Python (3.11.4)
- Django (4.0)
- Django REST framework (3.14.0)
- Other dependencies

## Installation

1. Clone this repository: ```git clone https://github.com/suyashXD/neofi.git\```
2. Navigate to the project directory: ```cd neofi```
3. Install Python dependencies: ```pip install -r requirements.txt```
4. Migrate the database: ```python manage.py migrate```
5. Start the development server: ```python manage.py runserver```

## Usage

### User Registration

To register a new user, make a POST request to the registration endpoint:

```
curl -X POST http://127.0.0.1:8000/api/register/ -d "username=yourusername&password=yourpassword&email=youremail@example.com&first_name=John&last_name=Doe"
```

### User Login

To log in as an existing user, make a POST request to the login endpoint:

```
curl -X POST http://127.0.0.1:8000/api/login/ -d "username=yourusername&password=yourpassword"
```

### Get Online Users

To retrieve a list of online users, make a GET request to the online users endpoint:

```
curl -H "Authorization: Token <your-auth-token>" http://127.0.0.1:8000/api/get-online-users/
```

### Start a Chat

To start a chat with another user, make a POST request to the chat start endpoint:

```
curl -X POST http://127.0.0.1:8000/api/chat/start/ -H "Authorization: Token <your-auth-token>" -d "receiver=<receiver-username>"
```

### Send a Chat Message

To send a chat message to another user, make a POST request to the chat send endpoint:

```
curl -X POST http://127.0.0.1:8000/api/chat/send/ -H "Authorization: Token <your-auth-token>" -d "receiver=<receiver-username>&message=your-message"
```

### Suggested Friends

To get a list of suggested friends for a user, make a GET request to the suggested friends endpoint by providing the user's ID:

```
curl -H "Authorization: <Token your-auth-token>" http://127.0.0.1:8000/api/suggested-friends/<your-user-id>/
```

