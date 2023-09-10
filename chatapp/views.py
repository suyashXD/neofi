# views.py
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
def get_online_users_view(request):
    if request.method == 'GET':
        # Implement logic to retrieve online users from your database
        # You can use the UserProfile model to check user's online status
        # online_users = UserProfile.objects.filter(is_online=True)
        online_users = []  # Replace with your logic to fetch online users
        return Response(online_users, status=status.HTTP_200_OK)

@api_view(['POST'])
def start_chat_view(request):
    if request.method == 'POST':
        # Implement logic to start a chat with another user
        # You might need to create a Chat model and manage chat sessions
        # Be sure to validate user availability and recipient's online status
        # Return an appropriate response based on success or failure
        return Response({'message': 'Chat started successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def send_message_view(request):
    if request.method == 'POST':
        # Implement logic to send a message
        # You'll need to validate recipient's online status before sending
        # Save the message in your database or message queue and return a success response
        return Response({'message': 'Message sent successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def recommended_friends_view(request, user_id):
    if request.method == 'GET':
        # Implement your recommendation algorithm to find recommended friends for the user
        # You can use the provided JSON file to fetch user data
        # Return a list of recommended friends based on your algorithm
        # For example, you can return the top 5 recommended friends
        recommended_friends = []  # Implement logic to fetch recommended friends
        return Response(recommended_friends, status=status.HTTP_200_OK)
