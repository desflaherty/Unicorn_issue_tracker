from django.shortcuts import render,reverse,redirect, get_object_or_404
from .forms import BugsForm
from .models import Bugs
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
                return redirect(bugs, id)
      
    else:
        form = BugsForm(instance=bugs)
    return render(request, 'add_bug.html', {'add_edit': add_edit,
                                               'form': form})