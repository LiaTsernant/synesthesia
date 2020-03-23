from django.shortcuts import render, redirect
from .models import Note, Person, Picture
from .forms import PersonForm, ProfileForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

# CREATE Note only if logged in
@login_required
def new_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('detail', note.id)
    else:
        form = NoteForm()
    context = {'form': form }
    return render(request, 'notes/note_form.html', context)

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

# CREATE picture only if logged in
class PictureCreate(LoginRequiredMixin, CreateView):
    model = Picture
    fields = '__all__'

# UPDATE picture only if logged in
class PictureUpdate(LoginRequiredMixin, UpdateView):
    model = Picture
    fields = ['name', 'link', 'description']

# DELETE picture only if logged in
class PictureDelete(LoginRequiredMixin, DeleteView):
    model = Picture
    success_url = '/pictures/'

# ---------------------------------------------------------------------------------------------------- Authorization

def signup(request):
    error_message = ''

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    user_form = UserCreationForm(request.POST)
    context = {'user_form': user_form ,'error_message': error_message}

    return render(request, 'registration/signup.html', context)

# ---------------------------------------------------------------------------------------------------------------------------

#SHOW and UPDATE user only if logged in
@login_required
def profile(request, username):
    error_message = ''
    success_message = ''
    user = User.objects.filter(username=username).first()

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            user = form.save(commit=False)
            if User.objects.filter(email=user.email).first():
                error_message = 'Email already exist'
                context = {'form':form, 'error_message': error_message, 'success_message': success_message}
                return render(request, 'user/profile_form.html', context)
            user = form.save()
            request.user = user
            success_message = 'Your profile has been updated!'
            context = {'form':form, 'error_message': error_message, 'success_message': success_message}
            return render(request, 'user/profile_form.html', context)
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'user/profile_form.html', {'form': form})

#Confirm deleting user only if logged in
@login_required
def confirm_delete_user(request, username):
    user = User.objects.filter(username=username)[0]
    return render(request, 'user/confirm_delete_user.html', {'user': user})

# DELETE user only if logged in
@login_required
def delete_profile(request, username):
    if request.method == 'POST':
        user = User.objects.filter(username=username).first()
        user.delete()
    return redirect('home')