from django.shortcuts import render, redirect
from .models import Note, Person, Picture
from .forms import PersonForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# ---------------------------------------------------------------------------------------------------- ABOUT AND HOME PAGES

# Project's home page
def home(request):
    return render(request, 'home.html')

# About the project
def about(request):
    return render(request, 'about.html')

# ---------------------------------------------------------------------------------------------------- NOTES 

# INDEX notes
def notes_index(request):
    notes = Note.objects.all()
    return render(request, 'notes/index.html', { 'notes': notes })

# SHOW notes
def notes_detail(request, note_id):
    note = Note.objects.get(id = note_id)
    unassociated_pictures = Picture.objects.exclude(id__in = note.pictures.all().values_list('id'))
    person_form = PersonForm()
    return render(request, 'notes/detail.html', {
        'note': note,
        'person_form': person_form,
        'pictures': unassociated_pictures
    })

# Add association between note and picture
def assoc_picture(request, note_id, picture_id):
    Note.objects.get(id=note_id).pictures.add(picture_id)
    return redirect('detail', note_id)

# Add guest's record on the page
def add_person(request, note_id):
    form = PersonForm(request.POST)
    if form.is_valid():
        new_person = form.save(commit=False)
        new_person.note_id = note_id
        new_person.save()
    return redirect('detail', note_id=note_id)

# ---------------------------------------------------------------------------------------------------- PICTURE CRUD

# INDEX pictures class View
class PictureList(ListView):
    model = Picture

# INDEX picture manual interpretation of class view.
def pictures_index(request):
    pics = Picture.objects.all()
    return render(request, 'main_app/picture_index.html', {
        'pictures': pics
    })

# SHOW picture
class PictureDetail(DetailView):
    model = Picture

# CREATE picture
class PictureCreate(CreateView):
    model = Picture
    fields = '__all__'

# UPDATE picture
class PictureUpdate(UpdateView):
    model = Picture
    fields = ['name', 'link', 'description']

# DELETE picture
class PictureDelete(DeleteView):
    model = Picture
    success_url = '/pictures/'

# ---------------------------------------------------------------------------------------------------- Authorization

def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}

    return render(request, 'registration/signup.html', context)

