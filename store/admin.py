from django.contrib import admin

# Register your models here.
from .models import Product, Cart, CartItem, Order, OrderItem

admin.site.register(Product)
# 註冊Product模型, 以便在Django 管理後台中管理商品.

class CartItemInline(admin.TabularInline):
    model = CartItem
# 創建一個內聯類別, 用於 Cart 管理頁面中直接編輯 CartItem.

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
# 註冊 Cart 模型, 並指定 CartItemInline 作為內聯, 這樣在 Cart 管理頁面中就可以直接編輯 CartItem.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
# 創建一個內聯類別, 用於 Order 管理頁面中直接編輯 OrderItem.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
# 註冊 Order 模型, 並指定 OrderItemInline 作為內聯, 這樣在 Order 管理頁面中就可以直接編輯 OrderItem.
