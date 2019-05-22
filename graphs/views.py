from django.shortcuts import render


def featuresgraphs(request):
    """A view that displays the fetures graphs"""
    return render(request, "features-graphs.html")
