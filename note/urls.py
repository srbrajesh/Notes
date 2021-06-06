from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.index, name='index'),
	path('addNote/', views.addNote, name='addNote'),
	path('deleteNote/<int:note_id>/', views.deleteNote, name="deleteNote"),
]