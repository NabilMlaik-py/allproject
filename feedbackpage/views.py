from django.shortcuts import render
from .forms import *
from .models import feedbackperson
from django.http import *


def index(request):
    if request.method == 'POST':
        form = feedback_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/feedbackpage/')
        else:
            form = feedback_form()
        return render(request, 'feedback.html', {'form': form})
    feedbackpage = feedbackperson.objects.all()
    return render(request, 'feedback.html',
                  {'feedbackperson': feedbackperson})

