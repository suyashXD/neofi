from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer, UserLoginSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .models import UserProfile
from .serializers import UserProfileSerializer

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ChatSession, Message


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('login')


@api_view(['POST'])
def user_registration_view(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(ObtainAuthToken):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def get_user_by_username_view(request, username):
    if request.method == 'GET':
        user = User.objects.filter(username=username).first()

        if user is not None:
            return Response(user.to_json(), status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_chat_session_by_ids_view(request, sender_id, recipient_id):
    if request.method == 'GET':
        chat_session = ChatSession.objects.filter(sender_id=sender_id, recipient_id=recipient_id).first()

        if chat_session is not None:
            return Response(chat_session.to_json(), status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Chat session not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_messages_by_chat_session_id_view(request, chat_session_id):
    if request.method == 'GET':
        messages = Message.objects.filter(chat_session_id=chat_session_id).order_by('-timestamp')

        return Response([message.to_json() for message in messages], status=status.HTTP_200_OK)




@api_view(['GET'])
def get_online_users_view(request):
    if request.method == 'GET':
        online_users = UserProfile.objects.filter(is_online=True)
        serializer = UserProfileSerializer(online_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def start_chat_view(request):
    if request.method == 'POST':
        sender_id = request.data['sender_id']
        recipient_id = request.data['recipient_id']

        # Check if both users are online
        sender_is_online = UserProfile.objects.get(id=sender_id).is_online
        recipient_is_online = UserProfile.objects.get(id=recipient_id).is_online

        if sender_is_online and recipient_is_online:
            # Create a new chat session and start the chat
            chat_session = ChatSession.objects.create(sender_id=sender_id, recipient_id=recipient_id)
            return Response({'message': 'Chat started successfully'}, status=status.HTTP_200_OK)
        else:
            # Return an error message if either user is offline
            if not sender_is_online:
                return Response({'message': 'Sender is offline'}, status=status.HTTP_400_BAD_REQUEST)
            elif not recipient_is_online:
                return Response({'message': 'Recipient is offline'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def send_message_view(request):
    if request.method == 'POST':
        sender_id = request.data['sender_id']
        recipient_id = request.data['recipient_id']
        message_content = request.data['message_content']

        # Check if the recipient is online
        recipient_is_online = UserProfile.objects.get(id=recipient_id).is_online

        if recipient_is_online:
            # Save the message in the database
            Message.objects.create(sender_id=sender_id, recipient_id=recipient_id, content=message_content)
            return Response({'message': 'Message sent successfully'}, status=status.HTTP_200_OK)
        else:
            # Return an error message if the recipient is offline
            return Response({'message': 'Recipient is offline'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def recommended_friends_view(request, user_id):
    if request.method == 'GET':
        # Implement your recommendation algorithm to find recommended friends for the user
        # You can use the provided JSON file to fetch user data
        # Return a list of recommended friends based on your algorithm
        # For example, you can return the top 5 recommended friends
        recommended_friends = []  # Implement logic to fetch recommended friends
        return Response(recommended_friends, status=status.HTTP_200_OK)
