from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produk/<int:id>/', views.detail_produk, name='detail'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:produk_id>/', views.add_to_cart, name='add_to_cart'),
    path('update-cart/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('process-checkout/', views.process_checkout, name='process_checkout'),
    path('pembayaran/<str:order_id>/', views.pembayaran, name='pembayaran'),
    path('konfirmasi-pembayaran/<str:order_id>/', views.konfirmasi_pembayaran, name='konfirmasi_pembayaran'),
    path('search/', views.search_produk, name='search'),
    path('kategori/<str:kategori>/', views.filter_kategori, name='filter_kategori'),
]