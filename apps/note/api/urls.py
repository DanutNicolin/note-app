from django.urls import path
from .views import NotesListCreateView, NotesDetailView
urlpatterns = [
    path('notes/', NotesListCreateView.as_view()),
    path('note/<pk>', NotesDetailView.as_view()),
]