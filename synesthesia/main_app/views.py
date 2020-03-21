from django.shortcuts import render, redirect
from .models import Note, Person, Picture
from .forms import PersonForm, ProfileForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

# CREATE Note
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
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = ProfileForm()
    context = {'form': form, 'error_message': error_message}

    return render(request, 'registration/signup.html', context)

# ---------------------------------------------------------------------------------------------------------------------------

# @login_required
def profile(request, user_id):
    # print(request.user)
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            print(f"USER IS {user}")
            request.user = user

        return redirect ('profile', user_id)
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'user/profile_form.html', {'form': form})



# def show_profile(request, user_id):
#     # Finds my user
#     user = User.objects.get(id=user_id)
#     print(user)

#     user_form = UserChangeForm(request.POST, instance=user)

#     # Stores profile form <label for="id_location">Location City:</label></th><td><input type="text" name="location" value="San Francisco, CA" maxlength="200" required id="id_location">
#     profile_form = ProfileForm()
#     print(profile_form)

#     return render(request, 'user/profile_form.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })

# def update_profile(request, user_id):
#     if request.method == 'POST':
#         user_form = UserChangeForm(request.POST, instance=request.user)
#         print(user_form)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if (profile_form.is_valid() and user_form.is_valid()):
#             user_form.save()
#             profile_form.save()
#             return redirect('show_profile')
#     else:
#         user_form = UserChangeForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'user/profile_form.html', {
#         'ures_form': user_form,
#         'profile_form': profile_form
#     })
