from django.urls import path
from .views import *

urlpatterns = [
    path('sign-in/', LoginView, name = 'login'),
    path('sign-out/', LogoutView, name = 'logout'),
    path('sign-up/', RegisterView, name = 'register'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
]
