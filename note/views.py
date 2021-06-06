from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import NewNote
# Create your views here.

# login
def home(request):
	if not request.user.is_authenticated:
		return render(request, "note/login.html", {"message":None})
	context = {
		"user":request.user
	}
	return HttpResponseRedirect(reverse('index'))

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('index'))
	else:
		return render(request, "note/login.html", {"message":"Invalid Credential"})

def logout_view(request):
	logout(request)
	return render(request, "note/login.html", {"message":"Logged Out"})
# login end

# start notes
def index(request):
    context = {
    "all_notes":NewNote.objects.all()
    }
    return render(request, "note/base.html", context)

def addNote(request):
	c = request.POST["content"]
	new_item = NewNote(content=c)
	new_item.save()
	return HttpResponseRedirect(reverse('index'))

def deleteNote(request, note_id):
	item_to_delete = NewNote.objects.get(id=note_id)
	item_to_delete.delete()
	return HttpResponseRedirect(reverse('index'))

# end Notes