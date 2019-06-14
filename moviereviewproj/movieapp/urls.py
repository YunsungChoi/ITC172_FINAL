from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getmovies/', views.getmovies, name='movies'),
    path('getreviews/', views.getreviews, name='reviews'),
    path('getgenres/', views.getgenres, name='genres'),
    path('moviedetails/<int:id>', views.moviedetails, name='moviedetails'),
    path('newMovie/', views.newMovie, name='newmovie'),
    path('newGenre/', views.newGenre, name='newgenre'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    
]