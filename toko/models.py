from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=200)
    harga = models.IntegerField()
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='produk/')
    stok = models.IntegerField()

    def __str__(self):
        return self.nama


class Pesanan(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('dibayar', 'Dibayar'),
    )

    nama_pembeli = models.CharField(max_length=100)
    alamat = models.TextField()
    total_harga = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    bukti_bayar = models.ImageField(upload_to='bukti/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ItemPesanan(models.Model):
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.IntegerField()