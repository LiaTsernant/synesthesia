# URLs for the main app
from django.urls import path
from . import views

urlpatterns = [
    # -------------------------------------------------------------------------------Note

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # INDEX notes
    path('notes/', views.notes_index, name='index'),
    # CREATE note
    path('notes/new/', views.new_note, name='new_note'),
    # # SHOW note
    path('notes/<int:note_id>', views.notes_detail, name='detail'),
    # # UPDATE note
    # path('notes/<int:note_id>/edit', views.notes_update, name='note_update'),
    # # DELETE note
    # path('notes/<int:note_id>/delete', views.notes_delete, name='note_delete'),
    # -------------------------------------------------------------------------------- Guest

    # CREATE guest's record with his  name and color
    path('notes/<int:note_id>/add_person', views.add_person, name='add_person'),

    # -------------------------------------------------------------------------------- Note-Picture(ManyToMany) association
    # Associate picture with a note
    path('notes/<int:note_id>/assoc_picture/<int:picture_id>/', views.assoc_picture, name='assoc_picture'),

    # -------------------------------------------------------------------------------- Picture

    path('pictures/', views.pictures_index, name="pictures_index"),
    path('pictures/<str:art_name>/', views.art_detail, name="picture_detail"),
    path('pictures/create', views.create_art, name="pictures_create"),
    path('pictures/<str:art_name>/update', views.update_art, name="pictures_update"),
    path('pictures/<str:art_name>/confirm_delete/', views.confirm_delete, name="pictures_confirm_delete"),

    path('pictures/<str:art_name>/delete/', views.delete_art, name="pictures_delete"),

    # -------------------------------------------------------------------------------- User
    # CREATE user
    path('signup', views.signup, name='signup'),

    #SHOW user and UPDATE
    path('<str:username>/', views.profile, name="profile"),

    # Delete user
    path('<str:username>/delete/', views.delete_profile, name="delete_profile"),
    path('<str:username>/confirm_delete', views.confirm_delete_user, name="confirm_delete_user"),

]