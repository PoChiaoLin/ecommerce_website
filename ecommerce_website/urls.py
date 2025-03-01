"""
URL configuration for ecommerce_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import product_list, about, add_to_cart, view_cart, checkout, order_success 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name = "product_list"),
    path("about/", about, name = "about"),
    path("add_to cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("view_cart/", view_cart, name="view_cart"),
    path("checkout/", checkout, name="checkout"),
    path("order_success/", order_success, name="order_success"),
]
