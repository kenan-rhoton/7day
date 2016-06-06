from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from .models import Post, Section

def homepage(request):
    posts = Post.objects.all()
    sections = Section.objects.all()
    can_post = request.user.has_perm('website.add_post')
    can_delete = request.user.has_perm('website.delete_post')
    return render(request, 'website/homepage.html', {
        'posts':posts,
        'sections':sections,
        'can_post': can_post,
        'can_delete': can_delete
        })

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

def add_post(request):
    if request.method == 'POST':
        can_post = request.user.has_perm('website.add_post')
        if can_post:
            if request.POST['post_section'] != "":
                section = get_object_or_404(Section, pk=request.POST['post_section'])
                p = Post(title=request.POST['post_title'], content=request.POST['post_content'])
                p.save()
                p.addSection(section)
                p.save()
                section.save()
            else:
                p = Post(title=request.POST['post_title'], content=request.POST['post_content'])
                p.save()

    return HttpResponseRedirect(reverse('website:HomePage'))

def delete_post(request, post_id):
    can_delete = request.user.has_perm('website.delete_post')
    if can_delete:
        p = get_object_or_404(Post, pk=post_id)
        p.delete()
    return HttpResponseRedirect(reverse('website:HomePage'))

def view_post(request, post_id):
    p = get_object_or_404(Post, pk=post_id)
    sections = Section.objects.all()
    can_delete = request.user.has_perm('website.delete_post')
    return render(request, 'website/postpage.html', {
        'post': p,
        'sections':sections,
        'can_delete': can_delete
        })

