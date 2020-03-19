from django.shortcuts import render, redirect
from .models import Note, Person, Picture
from .forms import PersonForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def notes_index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', { 'notes': notes })

def notes_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    unassociated_pictures = Picture.objects.exclude(id__in = note.pictures.all().values_list('id'))
    person_form = PersonForm()
    return render(request, 'notes/detail.html', {
        'note': note,
        'person_form': person_form,
        'pictures': unassociated_pictures
    })

def assoc_picture(request, note_id, picture_id):
    Note.objects.get(id=note_id).pictures.add(picture_id)
    return redirect('detail', note_id)

def add_person(request, note_id):
    form = PersonForm(request.POST)
    if form.is_valid():
        new_person = form.save(commit=False)
        new_person.note_id = note_id
        new_person.save()
    return redirect('detail', note_id=note_id)

# --------------------------------------------------------------------------------

# INDEX pictures
class PictureList(ListView):
    model = Picture

def pictures_index(request):
    pics = Picture.objects.all()
    return render(request, 'main_app/picture_index.html', {
        'pictures': pics
    })

# # SHOW picture
class PictureDetail(DetailView):
    model = Picture

# Create picture
class PictureCreate(CreateView):
    model = Picture
    fields = '__all__'

class PictureUpdate(UpdateView):
    model = Picture
    fields = ['name', 'link', 'description']

class PictureDelete(DeleteView):
    model = Picture
    success_url = '/pictures/'
