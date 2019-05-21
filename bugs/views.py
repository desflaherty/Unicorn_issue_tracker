from django.shortcuts import render,reverse,redirect, get_object_or_404
from .models import Bugs
from django.contrib.auth.models import User
from django.utils import timezone

def all_bugs(request):
    bugs = Bugs.objects.all()
    return render(request, 'bugs.html', {'bugs': bugs})
