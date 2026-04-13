from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk, Pesanan, ItemPesanan

def home(request):
    produk = Produk.objects.all()
    return render(request, 'home.html', {'produk': produk})


def detail_produk(request, id):
    produk = get_object_or_404(Produk, id=id)
    return render(request, 'detail.html', {'produk': produk})


def checkout(request, id):
    produk = get_object_or_404(Produk, id=id)

    if request.method == 'POST':
        jumlah = int(request.POST['jumlah'])
        total = produk.harga * jumlah

        pesanan = Pesanan.objects.create(
            nama_pembeli=request.POST['nama'],
            alamat=request.POST['alamat'],
            total_harga=total
        )

        ItemPesanan.objects.create(
            pesanan=pesanan,
            produk=produk,
            jumlah=jumlah
        )

        return redirect('pembayaran', pesanan.id)

    return render(request, 'checkout.html', {'produk': produk})


def pembayaran(request, id):
    pesanan = get_object_or_404(Pesanan, id=id)

    if request.method == 'POST':
        pesanan.bukti_bayar = request.FILES['bukti']
        pesanan.status = 'dibayar'
        pesanan.save()
        return redirect('home')

    return render(request, 'pembayaran.html', {'pesanan': pesanan})