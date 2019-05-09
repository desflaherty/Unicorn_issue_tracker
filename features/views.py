from django.shortcuts import render,reverse,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Features, UpvoteFeature
from django.contrib.auth.models import User
from .forms import FeaturesForm

def all_features(request):
    features = Features.objects.all()
    return render(request, 'features.html', {'features': features})


def feature_detail(request, id):
    """Renders a view of an individual feature"""

    features = get_object_or_404(Features, id=id)
    
    upvotes = UpvoteFeature.objects.filter(upvoted_feature=features)
    
    upvoted = False
    user = str(request.user)
    for item in upvotes:
        item = str(item)
        if item == user:
            upvoted = True

    features.save()


    return render(request, "feature_details.html", {'upvoted': upvoted,
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
                                               
                                               
@login_required
def upvote_feature(request):
    """Adds one upvote point to the feature  """

    cart = request.session.get('cart', {})
    upvote_list = []

    for id, quantity in cart.items():
        feature = get_object_or_404(Features, pk=id)
        upvote_list.append(id)

    for id in upvote_list:
        feature_name = get_object_or_404(
            Features, id=id)
        try:
            upvote = get_object_or_404(
                UpvoteFeature, user=request.user, upvoted_feature=feature_name)
        except:
            upvote = UpvoteFeature()
        upvote.user = request.user
        upvote.upvoted_feature = feature_name
        feature_name.upvotes += 1
        feature_name.save()
        upvote.save()
    request.session['cart'] = {}
    return redirect(reverse('index'))                                               