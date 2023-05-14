from django.urls import path
from .views import UserListView, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='user'),
]


