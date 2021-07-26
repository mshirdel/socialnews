from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateStoryView.as_view()),
    path("update/<int:pk>/", views.RetrieveUpdateDestroyStoryView.as_view())
]
