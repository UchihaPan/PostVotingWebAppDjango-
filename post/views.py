from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, 'base.html')


@login_required()
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url'] and request.POST['description'] and request.FILES['icon'] and \
                request.FILES['image']:
            post = Post()
            post.user = request.user
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.description = request.POST['description']
            post.icon = request.FILES['icon']
            post.image = request.FILES['image']
            post.save()
            return redirect('home')
        else:
            return render(request, 'post/create.html', {'errors': 'Please enter all the fields'})

    return render(request, 'post/create.html')


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
