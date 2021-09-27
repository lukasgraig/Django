from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import BlogForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogs/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogs/post-detail.html'

@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
    # create object of form
        form = BlogForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('home')

    else:
        form = BlogForm()
  
    return render(request, "blogs/create-blog.html", {'form': form})
