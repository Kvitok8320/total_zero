from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm, Product
from django.views.decorators.http import require_POST
from .cart import Cart

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=int(request.POST.get('quantity', 1)))
    return redirect('cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'])
        cart.clear()
        return render(request, 'cart/order_created.html', {'order': order})
    return redirect('cart_detail')

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
