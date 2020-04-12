from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Entry

class HomepageView(generic.ListView):
    paginate_by = 4
    template_name = 'blog/index.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        return Entry.objects.all()[::-1]

class EntryView(generic.DetailView):
    model = Entry
    template_name = 'blog/entry.html'

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def donate(request):
    return render(request, 'blog/donate.html')