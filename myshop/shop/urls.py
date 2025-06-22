from django.urls import path
from . import views
from .views import CustomLoginView  # Импорт из текущего приложения

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart_detail, name='cart_detail'),  # Добавьте это перед категориями
    path('checkout/', views.checkout_view, name='checkout'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:order_item_id>/', views.cart_remove, name='cart_remove'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),

]