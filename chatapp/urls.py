from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_registration_view, name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('online-users/', views.get_online_users_view, name='online-users'),
    path('chat/start/', views.start_chat_view, name='start-chat'),
    path('chat/send/', views.send_message_view, name='send-message'),
    path('suggested-friends/<int:user_id>/', views.recommended_friends_view, name='recommended-friends'),
]
