from django.urls import path
from . import views

urlpatterns = [
    # path("<slug:url>/", views.youtubeAPI),
    path("", views.YoutubeVideo.as_view()),
]
