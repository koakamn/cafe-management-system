from django.shortcuts import render,redirect,get_object_or_404
from menu.models import Product
from .cart import  Cart
from .forms import CheckoutForm
from .models import OrderItem


def cart_add(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)

    cart.add(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart=Cart(request)

    return render(request, 'orders/cart_detail.html',{
        'cart':cart,
    })
def cart_remove(request,product_id):
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)

    cart.remove(product)
    return redirect('cart_detail')

def cart_update(request,product_id,quantity):
    cart=Cart(request)

    product=get_object_or_404(Product,id=product_id)
    cart.update(product,quantity)

    return redirect('cart_detail')

def checkout(request):
    cart=Cart(request)

    if request.method=='POST':
        form=CheckoutForm(request.POST)
        if form.is_valid():
            order=form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['product'].price,
                    quantity=item['quantity']
                )

            request.session['cart']={}
            return redirect('menu_list')
    else:
        form=CheckoutForm()

    return render(request,'orders/checkout.html',{'form':form,'cart':cart})