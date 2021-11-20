from django.shortcuts import render
from django.views import generic
from django.utils import timezone

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

#class JournalEntriesView(generic.ListView):
#    template_name='parksApp/entries.html'
#    context_object_name='entry_list'
#    def get_queryset(self):
#        entry_list=JournalEntry.objects.all()
#        return entry_list