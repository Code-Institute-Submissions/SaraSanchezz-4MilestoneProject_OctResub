from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51IwmiWIhtQbRiixnzNtNnD0Sbyt39jmwuQ0XBd1zYRStP2I2Kr1GGeDwV4QW6SH6pF8jHduqbF263v8HBWXILK5700okT38ug7',
        'client_secret': 'test_client_secret',
    }
    return render(request, template, context)
