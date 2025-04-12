from django.urls import path
from . import views

urlpatterns = [
    path("", views.default, name='default'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_auth, name="login_auth"),  
    path("logout/", views.logout_auth, name="logout_auth"),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page') 
]