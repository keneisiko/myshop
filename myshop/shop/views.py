from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Order, OrderItem, CardData
from django.contrib.auth.decorators import login_required
from .forms import AddToCartForm, CardDataForm
from django.contrib import messages
from django.shortcuts import render
from .models import Product
from django.contrib.auth.views import LoginView


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products_by_category = {}
    for category in categories:
        products_by_category[category] = Product.objects.filter(category=category, available=True)
    cart_item_count = 0
    if request.user.is_authenticated:
        cart = Order.objects.filter(user=request.user, paid=False).first()
        cart_item_count = cart.items.count() if cart else 0
    return render(request, 'shop/product/list.html', {
        'products_by_category': products_by_category,
        'cart_item_count': cart_item_count,
        'request': request
    })



def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    form = AddToCartForm()
    return render(request, 'shop/product/detail.html', {
        'product': product,
        'form': form
    })


@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    # Получаем или создаем заказ
    order, created = Order.objects.get_or_create(
        user=request.user,
        paid=False
    )

    # Получаем или создаем элемент заказа
    order_item, created = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        defaults={'quantity': quantity, 'price': product.price}
    )

    if not created:
        order_item.quantity = quantity
        order_item.save()

    return redirect('shop:cart_detail')


@login_required
def cart_remove(request, order_item_id):
    order_item = get_object_or_404(OrderItem, id=order_item_id)
    order_item.delete()
    messages.success(request, 'Товар удален из корзины')
    return redirect('shop:cart_detail')


def cart_detail(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user, paid=False).first()
        cart_item_count = order.items.count() if order else 0
    else:
        order = None
        cart_item_count = 0

    return render(request, 'shop/cart/detail.html', {
        'order': order,
        'cart_item_count': cart_item_count,
        'request': request
    })


@login_required
def checkout_view(request):
    order = Order.objects.filter(user=request.user, paid=False).first()
    if not order or order.items.count() == 0:
        messages.error(request, 'Ваша корзина пуста.')
        return redirect('shop:cart_detail')

    if request.method == 'POST':
        payment_method = request.POST.get('payment')
        if payment_method == 'card':
            form = CardDataForm(request.POST)
            if form.is_valid():
                # Сохраняем данные карты
                CardData.objects.update_or_create(
                    order=order,
                    defaults={
                        'card_number': form.cleaned_data['card_number'],
                        'card_expiry': form.cleaned_data['card_expiry'],
                        'card_cvv': form.cleaned_data['card_cvv'],
                        'card_name': form.cleaned_data['card_name'],
                    }
                )
                request.session['card_data_saved'] = True
                messages.success(request, 'Данные карты сохранены!')
                return redirect('shop:checkout')
            else:
                messages.error(request, 'Ошибка в данных карты.')
        else:
            # Обработка других способов оплаты
            form = CardDataForm()  # Просто пустая форма, чтобы не было ошибки
    else:
        form = CardDataForm()

    card_data_saved = request.session.get('card_data_saved', False)
    return render(request, 'shop/checkout.html', {
        'order': order,
        'cart_item_count': order.items.count(),
        'form': form,
        'request': request,
        'card_data_saved': card_data_saved
    })

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    extra_context = {'hide_navbar': True}  # Скрываем навбар на странице входа