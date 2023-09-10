from django.urls import path
from .views import CustomLoginView, CustomUserCreationView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomUserCreationView.as_view(), name='register'),
]
