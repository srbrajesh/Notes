from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name='home'),
	path("login", views.login_view, name='login'),
	path("logout", views.logout_view, name='logout'),
	path('home/', views.index, name='index'),
	path('addNote/', views.addNote, name='addNote'),
	path('deleteNote/<int:note_id>/', views.deleteNote, name="deleteNote"),
]