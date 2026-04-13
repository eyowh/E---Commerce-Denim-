from django.contrib import admin
from .models import Produk, Pesanan, ItemPesanan

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga', 'stok')
    search_fields = ('nama',)


@admin.register(Pesanan)
class PesananAdmin(admin.ModelAdmin):
    list_display = ('nama_pembeli', 'total_harga', 'status')


@admin.register(ItemPesanan)
class ItemPesananAdmin(admin.ModelAdmin):
    list_display = ('produk', 'jumlah')