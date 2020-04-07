from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def index(request):
    return render(request, 'pages/index.html', {})


@login_required
def postView(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            user_id = request.user
            x = Post(title=title, description=description, user_id=user_id)
            x.save()
    else:
        form = PostForm()
    return render(request, 'pages/post.html', {
        'form':form
    })

@login_required
def allPost(request):
    ls = Post.objects.all()
    return render(request, "pages/allpost.html", {
        'ls' : ls
    })

@login_required
def myPost(request):
    user_id = request.user
    ls = Post.objects.filter(user_id=user_id)
    return render(request,"pages/mypost.html", {
        'ls': ls,
    }
    )