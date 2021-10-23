from django.shortcuts import render

# Create your views here.


def view_reviews(request):
    """ A view to show reviews page """

    return render(request, 'reviews/reviews.html')
