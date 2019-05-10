from django.shortcuts import render,reverse,redirect, get_object_or_404
from .forms import FeaturesForm
from .forms import CommentForm
from .models import Comments
from django.contrib.auth.decorators import login_required
from .models import Features, UpvoteFeature
from django.contrib.auth.models import User
from django.utils import timezone


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

    features.views += 1
    features.save()


    return render(request, "feature_details.html", {'upvoted': upvoted,
                                                   'items': features
                                                   })



@login_required
def add_comment_features(request, id=id):
    """Saves a posted comment  """

    feature = get_object_or_404(Features, id=id)
   

    comment_form = CommentForm(request.POST, request.FILES)
    if comment_form.is_valid():
        instance = comment_form.save(commit=False)
        instance.username = request.user
        
        instance.feature_ticket = feature
        
        comment_form.save()

    return redirect(feature_detail, id)



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
                if str(form.status) == 'Doing':
                    form.waiting_date = None
                    form.in_progress_date = timezone.now()
                elif str(form.status) == 'Done':
                    form.in_progress_date = None
                    form.completion_date = timezone.now()
        if features == None:
                form.username = request.user
                form.views = -1
                form.created_date = timezone.now()
                form.waiting_date = timezone.now()
                form.save()
                return redirect(reverse(all_features))
                
        else:
                form.username = features.username 
                form.views -= 1
                form.save()
                return redirect(feature_detail, id)
      
    else:
        form = FeaturesForm(instance=features)
    return render(request, 'add_feature.html', {'add_edit': add_edit,
                                               'form': form})
                                               
                                               
@login_required
def upvote_feature(request):
    """Adds one upvote point to the feature  """

    cart = request.session.get('cart', {})
    upvote_list = []

    for id  in cart.items():
       
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