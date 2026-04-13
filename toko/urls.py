from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produk/<int:id>/', views.detail_produk, name='detail'),
    path('checkout/<int:id>/', views.checkout, name='checkout'),
    path('pembayaran/<int:id>/', views.pembayaran, name='pembayaran'),
]