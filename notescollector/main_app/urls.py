# URLs for the main app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('notes/', views.notes_index, name='index'),
    path('notes/<int:note_id>', views.notes_detail, name='detail'),
    path('notes/<int:note_id>/add_person', views.add_person, name='add_person'),
    path('notes/<int:note_id>/assoc_picture/<int:picture_id>/', views.assoc_picture, name='assoc_picture'),

    # --------------------------------------------------------------------------------

    path('pictures/', views.pictures_index, name="pictures_index"),
    path('pictures/<int:pk>/', views.PictureDetail.as_view(), name="picture_detail"),
    path('pictures/create/', views.PictureCreate.as_view(), name="pictures_create"),
    path('pictures/<int:pk>/update/', views.PictureUpdate.as_view(), name="pictures_update"),
    path('pictures/<int:pk>/delete/', views.PictureDelete.as_view(), name="pictures_delete"),



]