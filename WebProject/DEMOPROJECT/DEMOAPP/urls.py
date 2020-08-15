from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('home', views.home, name='home-page'),
    path('events', views.events, name='event-page'),
    path('aboutClique', views.aboutClique, name='about-page'),
    path('interestship1', views.interestship1, name='interestship1-page'),
    path('informativeTalks', views.informativeTalks, name='informativeTalks-page'),
    path('triviaEve', views.triviaEve, name='triviaEve-page'),
]

