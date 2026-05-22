#notes/views.py
from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Note

class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/note_list.html"

class PopularNoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"
    queryset = Note.objects.filter(likes__gte=1)

class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"

def detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        raise Http404("Note doesn't exist")
    return render(request, 'notes/notes_detail.html', {'note': note})