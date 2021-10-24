from django.shortcuts import render
from .models import Post

# Create your views here.


def view_community(request):
    """ A view to show community page """
    posts = Post.objects.all()

    return render(request, 'community/community.html', {'posts': posts})
