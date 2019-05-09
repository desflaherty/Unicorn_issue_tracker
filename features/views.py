from django.shortcuts import render,reverse,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Features
from django.contrib.auth.models import User
from .forms import FeaturesForm

def all_features(request):
    features = Features.objects.all()
    return render(request, 'features.html', {'features': features})


def feature_detail(request, id):
    """Renders a view of an individual feature"""

    features = get_object_or_404(Features, id=id)


    features.save()


    return render(request, "feature_details.html", {
                                                   'items': features
                                                   })








@login_required
def add_edit_feature(request, id=None):
    """Renders the add or edit page and saves features  """

    features = get_object_or_404(Features, id=id) if id else None
    user = str(request.user)
    add_edit = True
    if features == None:
        add_edit = False
    if request.method == "POST":
        form = FeaturesForm(request.POST, request.FILES, instance=features)
        
        if form.is_valid():
            form = form.save(commit=False)
        if user == 'admin' or user == 'testadmin':
                form.status = request.POST.get('status')    
            
        if features == None:
                form.username = request.user
                form.save()
                return redirect(reverse(all_features))
                
        else:
                form.username = features.username 
                form.save()
                return redirect(features, id)
      
    else:
        form = FeaturesForm(instance=features)
    return render(request, 'add_feature.html', {'add_edit': add_edit,
                                               'form': form})