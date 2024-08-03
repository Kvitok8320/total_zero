from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm
@login_required
def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_item_formset = OrderItemForm(request.POST)

        if order_form.is_valid() and order_item_formset.is_valid():
            order = order_form.save()
            order_item = order_item_formset.save(commit=False)
            order_item.order = order
            order_item.save()
            return redirect('order_success')
        else:
            order_form = OrderForm()
            order_item_formset = OrderItemForm()

        return render(request, 'order/create_order.html',
                      {'order_form': order_form, 'order_item_formset': order_item_formset})
    return render(request, 'order/create_order.html')

def order_success(request):
    return HttpResponse('<h2> Вы успешно создали заказ! </h2>')
