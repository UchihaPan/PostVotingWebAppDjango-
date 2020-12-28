from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path
from .views import home,Signup

urlpatterns = [
    path('',home,name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='post/login.html'), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),
]
