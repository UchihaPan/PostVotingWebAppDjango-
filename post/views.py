from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    posts=Post.objects.all()

    return render(request, 'post/home.html',{
'posts':posts
    })

@login_required
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/detail.html', {
        'post': post
    })

@login_required
def upvote(request, pk):
    post = Post.objects.get(pk=pk)

    if post.votes >= 1:
        return redirect('detail', pk )
    else:
        post.votes+=1
    post.save()
    return redirect('detail', pk)



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
            return redirect('detail', post.pk)
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
