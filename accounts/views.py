
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.http.response import Http404
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def user_profile(request, user):
    try:
        user = UserModel.objects.get(username=user)
    except UserModel.DoesNotExist:
        raise Http404(f"{user} does not exist")
    return render(request, 'registration/profile.html', {'user': user})