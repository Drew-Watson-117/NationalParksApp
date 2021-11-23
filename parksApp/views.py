from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.urls import reverse

from .models import Park, JournalEntry


class ParksHomeView(generic.ListView):
    template_name='parksApp/index.html'
    context_object_name='parks_list'
    def get_queryset(self):
        parks_list=Park.objects.all()
        return parks_list

class VisitedParksView(generic.ListView):
    template_name='parksApp/visited.html'
    context_object_name='parks_list'
    def get_queryset(self):
        parks_list=Park.objects.all()
        return parks_list

class MarkedParksView(generic.ListView):
    template_name='parksApp/marked.html'
    context_object_name='parks_list'
    def get_queryset(self):
        parks_list=Park.objects.all()
        return parks_list

class ParkDetailView(generic.DetailView):
    model=Park
    template_name="parksApp/park.html"

def toggleMark(request, park_id):
    park = get_object_or_404(Park, pk=park_id)
    park.marked = not park.marked
    park.save()
    return HttpResponseRedirect(reverse('parksApp:park',args=(park.id,)))

def toggleVisit(request, park_id):
    park = get_object_or_404(Park, pk=park_id)
    park.visited = not park.visited
    park.save()
    return HttpResponseRedirect(reverse('parksApp:park',args=(park.id,)))
    
def addEntry(request, park_id):
    park = get_object_or_404(Park, pk=park_id)
    new_entry= JournalEntry()
    new_entry.park=park
    try:
        new_entry.visitation_date=request.POST['date']
        new_entry.content=request.POST['content']
        new_entry.save()
    except:
        return render(request, "parksApp/park.html", {'park': park, 'error_message': "Please Do Not Leave Any Fields Blank"})
    else:
        return HttpResponseRedirect(reverse('parksApp:park',args=(park.id,)))

def deleteEntry(request, entry_id):
    entry = get_object_or_404(JournalEntry, pk=entry_id)
    entry.delete()
    return HttpResponseRedirect(reverse('parksApp:park',args=(park.id,)))
    