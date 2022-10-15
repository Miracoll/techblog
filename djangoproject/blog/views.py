from django.shortcuts import redirect, render
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def home(request):
    post = Post.objects.all()
    context = {'posts':post}
    return render(request,'blog/tech-index.html', context)

def createpost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post added successfully')
            return redirect('home')
    context = {'form':form}
    return render(request, 'blog/createpost.html', context)

def updatepost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('home')
    context = {'form':form}
    return render(request, 'blog/updatepost.html', context)