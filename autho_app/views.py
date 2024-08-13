from django.shortcuts import render
from .models import Topic

def index(request):
    # The home page for Authorization project
    return render(request, 'autho_app/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'registration': topics}
    return render(request, 'autho_app/registration.html', context)
