from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SandwichForm
from .models import Sandwich

@login_required
def order(request):
    if request.method == 'POST':
        form = SandwichForm(request.POST)
        if form.is_valid():
            sandwich = form.save(commit=False)
            sandwich.customer = request.user
            sandwich.save()
            return redirect('common:home')
    else:
        form = SandwichForm()
    context = {'form' : form}
    return render(request, 'order/order.html', context)

@login_required
def history(request):
    order_list = Sandwich.objects.filter(customer=request.user)
    context = {'order_list' : order_list}
    return render(request, 'order/order_history.html', context)