from django.shortcuts import render

def index(request):
    """ a view that displays the index page """
    return render(request,"index.html")
