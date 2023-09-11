from django.contrib import admin
from django.urls import path, include
from chatapp.chatroute import websocket_urlpatterns
urlpatterns = [
    path('api/', include('chatapp.urls')),
    path('ws/', include(websocket_urlpatterns)),
    path('admin/', admin.site.urls),
]