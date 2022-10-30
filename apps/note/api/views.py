from django.shortcuts import render
# from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework import generics

from ..models import Note
from .serializers import NoteSerializer
# Create your views here.

class NotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NotesListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer





# class NotesCreateView(CreateView):
#     model = NoteModel


# class NotesUpdateView(UpdateView):
#     model = NoteModel


# class NotesDeleteView(DeleteView):
#     model = NoteModel