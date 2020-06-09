from django.urls import path, include
from . import views


urlpatterns = [
    path('messages/', views.messages_display, name='messages_display'),
    path('new_message/', views.new_message, name='new_message')
]
