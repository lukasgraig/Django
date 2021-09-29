from django.contrib.auth.forms import UserCreationForm, UserModel
from django.http.response import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import logout
from blogs.models import Post

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def user_profile(request, user):
    try:
        user = UserModel.objects.get(username=user)
        post = Post.objects.filter(author=user)

    except UserModel.DoesNotExist:
        raise Http404(f"{user} does not exist")
    return render(request, 'registration/profile.html', {'post': post})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('blogs/post-detail.html')