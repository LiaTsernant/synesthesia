# URLs for the main app
from django.urls import path
from . import views

urlpatterns = [
    # -------------------------------------------------------------------------------Note

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # INDEX notes
    path('notes/', views.notes_index, name='index'),
    # SHOW note
    path('notes/<int:note_id>', views.notes_detail, name='detail'),

    # -------------------------------------------------------------------------------- Guest

    # CREATE guest's record with his  name and color
    path('notes/<int:note_id>/add_person', views.add_person, name='add_person'),

    # -------------------------------------------------------------------------------- Note-Picture(ManyToMany) association
    # Associate picture with a note
    path('notes/<int:note_id>/assoc_picture/<int:picture_id>/', views.assoc_picture, name='assoc_picture'),

    # -------------------------------------------------------------------------------- Picture

    path('pictures/', views.pictures_index, name="pictures_index"),
    path('pictures/<int:pk>/', views.PictureDetail.as_view(), name="picture_detail"),
    path('pictures/create/', views.PictureCreate.as_view(), name="pictures_create"),
    path('pictures/<int:pk>/update/', views.PictureUpdate.as_view(), name="pictures_update"),
    path('pictures/<int:pk>/delete/', views.PictureDelete.as_view(), name="pictures_delete"),

    # -------------------------------------------------------------------------------- User
    # CREATE user
    path('accounts/signup', views.signup, name='signup'),
]