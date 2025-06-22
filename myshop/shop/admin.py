from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from django.contrib import admin
from .models import Category, Product, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  # Теперь slug существует
    prepopulated_fields = {'slug': ('name',)}  # Теперь это будет работать

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'available']  # Добавили slug
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'available']
    readonly_fields = ['preview']

    def preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px;"/>', obj.image.url if obj.image else '')
    preview.short_description = 'Превью'
