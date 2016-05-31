from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from .models import Post

def homepage(request):
    posts = Post.objects.all()
    can_post = request.user.has_perm('website.add_post')
    return render(request, 'website/homepage.html', {'posts':posts, 'can_post': can_post})

def log_in(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)

    return HttpResponseRedirect(reverse('website:HomePage'))

def log_out(request):
    logout(request)

    return HttpResponseRedirect(reverse('website:HomePage'))
