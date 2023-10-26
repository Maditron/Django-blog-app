from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


def post(request, post):
    posts = Post.objects.all()
    for p in posts:
        if p.title == post:
            return render(request, 'blog/post.html',{'post_title':p.title, 'post_content':p.content})
    return HttpResponse('nothing to show')
    

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')