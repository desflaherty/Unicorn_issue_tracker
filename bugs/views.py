from django.shortcuts import render,reverse,redirect, get_object_or_404
from .forms import BugsForm
from .forms import CommentForm
from .models import BugComments
from .models import Bugs,UpvoteBug
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

def all_bugs(request):
    bugs = Bugs.objects.all()
    return render(request, 'bugs.html', {'bugs': bugs})


@login_required
def add_edit_bug(request, id=None):
    """Renders the add or edit page and saves bugs  """

    bugs = get_object_or_404(Bugs, id=id) if id else None
    user = str(request.user)
    add_edit = True
    if bugs == None:
        add_edit = False
    if request.method == "POST":
        form = BugsForm(request.POST, request.FILES, instance=bugs)
        
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
        if bugs == None:
                form.username = request.user
                form.views = -1
                form.created_date = timezone.now()
                form.waiting_date = timezone.now()
                form.save()
                return redirect(reverse(all_bugs))
                
        else:
                form.username = bugs.username 
                form.views -= 1
                form.save()
                return redirect(bug_detail, id)
      
    else:
        form = BugsForm(instance=bugs)
    return render(request, 'add_bug.html', {'add_edit': add_edit,
                                               'form': form})
                                               

def bug_detail(request, id):
    """Renders a view of an individual bug"""

    bugs = get_object_or_404(Bugs, id=id)
    
    upvotes = UpvoteBug.objects.filter(upvoted_bug=bugs)
    
    upvoted = False
    user = str(request.user)
    for item in upvotes:
        item = str(item)
        if item == user:
            upvoted = True

    comments = BugComments.objects.filter(bug_ticket=id).order_by('created_date')
    comments_number = comments.count()
    comment_form = CommentForm()
    bugs.views += 1
    bugs.save()

   
    return render(request, "bug_detail.html", {'upvoted': upvoted,
                                                   'items': bugs,
                                                   'comment_form': comment_form,
                                                   'comments': comments,
                                                   'comments_number':comments_number})                                          
                                               
@login_required
def add_comment_bugs(request, id=id):
    """Saves a posted bug  """

    bug = get_object_or_404(Bugs, id=id)
   

    comment_form = CommentForm(request.POST, request.FILES)
    if comment_form.is_valid():
        instance = comment_form.save(commit=False)
        instance.username = request.user
        instance.bug_ticket = bug
        
        comment_form.save()

    return redirect(bug_detail, id)
                                            
    
@login_required
def upvote_bug(request):
    """Adds one upvote point to the bug  """

    cart = request.session.get('cart', {})
    upvote_list = []

    for id,quantity in cart.items():
       bug = get_object_or_404(Bugs, pk=id)
       upvote_list.append(id)

    for id in upvote_list:
        bug_name = get_object_or_404(
            Bugs, id=id)
        try:
            upvote = get_object_or_404(
                UpvoteBug, user=request.user, upvoted_bug=bug_name)
        except:
            upvote = UpvoteBug()
        upvote.user = request.user
        upvote.upvoted_bug = bug_name
        bug_name.upvotes += 1
        bug_name.save()
        upvote.save()
    request.session['cart'] = {}
    return redirect(reverse('index'))                                             
                                               