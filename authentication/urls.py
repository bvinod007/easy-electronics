from django.urls import path
from . import views

urlpatterns = [
    path('user/register/', views.Register),
    path('user/login/', views.Login)
]