from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.


def home(request):
    return render(request,'base.html')


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'post/signup.html'

    def form_valid(self, form):
        view = super(Signup, self).form_valid(form)
        username, password = form.cleaned_data['username'], form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view