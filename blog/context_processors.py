from .models import Entry

def add_variable_to_context(request):
    return {
        'entries': Entry.objects.all().order_by('pub_date')[::-1][:2]
    }