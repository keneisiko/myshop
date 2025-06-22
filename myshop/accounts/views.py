from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, UserProfileForm
from .models import UserProfile
from shop.models import CardData, Order

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)
    card = None
    order = None
    # Ищем последний заказ пользователя, у которого есть связанные данные карты
    card_data = CardData.objects.filter(order__user=user).order_by('-created').first()
    if card_data:
        card = card_data
        order = card_data.order
        cart_item_count = order.items.count() if order else 0
    else:
        # fallback: если нет ни одной карты, считаем корзину по не оплаченному заказу
        order = Order.objects.filter(user=user, paid=False).first()
        cart_item_count = order.items.count() if order else 0
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            # Email не обновляем через профиль
            profile.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile, initial={'email': user.email})
    return render(request, 'accounts/profile.html', {
        'form': form,
        'profile': profile,
        'user': user,
        'card': card,
        'order': order,
        'cart_item_count': cart_item_count,
    })