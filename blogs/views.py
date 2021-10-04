from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import BlogForm, CommentForm
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogs/index.html'

'''class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blogs/post-detail.html'''

def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('post_detail', post.slug)

@login_required(login_url='login')
def create_blog(request):
    if request.method == 'POST':
    # create object of form
        form = BlogForm(request.POST)

        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.author = request.user
            task_list.save()


        return redirect('home')

    else:
        form = BlogForm()
  
    return render(request, "blogs/create-blog.html", {'form': form})

def post_detail(request, slug):
    template_name = 'blogs/post-detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})