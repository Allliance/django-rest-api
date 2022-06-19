
from django.urls import path
from . import views

urlpatterns = [
    path('presence/', views.presence, name='presence'),
    path('register/<str:username>/', views.register, name='presence'),
    path('unregister/', views.unregister, name='presence'),
    path('send_message/<str:username>', views.send_message, name='presence'),
]
