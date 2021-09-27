from django.views import generic
from django.shortcuts import render, redirect
from .models import CheckList
from .forms import CheckListForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
class CheckListView(generic.ListView):
    queryset = CheckList.objects.all()
    template_name = 'checklist/checklist.html'

@login_required(login_url='login')
def create_item(request):
    if request.method == 'POST':
        form = CheckListForm(request.POST or None)
        # check if form data is valid
        if form.is_valid():
            # save the form data to model
            form.save()
            return redirect('checklist')
    else:
        form = CheckListForm()
  
    return render(request, "checklist/create.html", {'form': form})

def update(request, id):
    done = CheckList.objects.get(id=id)
    if done.completed == True:
        done.completed = False
    else:
        done.completed = True
    done.save()
    return HttpResponseRedirect(reverse('checklist'))