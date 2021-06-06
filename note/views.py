from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import NewNote
# Create your views here.

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