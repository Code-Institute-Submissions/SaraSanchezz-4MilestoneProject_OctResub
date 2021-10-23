from django.shortcuts import render

# Create your views here.


def view_community(request):
    """ A view to show community page """

    return render(request, 'community/community.html')
