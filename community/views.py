from django.shortcuts import render, redirect
from .models import Post

from .forms import CommentForm

# Create your views here.


def view_community(request):
    """ A view to show community page """
    posts = Post.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('community/community.html', tittle=post.title)
    else:
        form = CommentForm()


    return render(request, 'community/community.html', {'posts': posts})


    