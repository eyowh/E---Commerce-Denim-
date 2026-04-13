# Catty Denim - E-Commerce Website Django

Sebuah website e-commerce modern berbasis Django yang menjual produk denim (celana jeans, jaket denim, kaos denim, dan aksesoris) dengan fitur lengkap dan tampilan modern menggunakan Tailwind CSS.

## Fitur Utama

### Backend (Django)
- **Model Produk**: Nama, harga, deskripsi, gambar, stok, kategori, diskon, best seller
- **Model Pesanan**: Informasi pembeli, alamat, total harga, status, ID unik
- **Model ItemPesanan**: Relasi antara pesanan dan produk dengan jumlah dan harga
- **Sesi Keranjang**: Cart functionality menggunakan Django sessions
- **QRIS Payment**: Generate QR Code otomatis untuk pembayaran
- **Admin Panel**: Manajemen produk dan pesanan yang user-friendly

### Frontend (Tailwind CSS)
- **Desain Modern**: Marketplace-style seperti Shopee/Tokopedia
- **Responsive Design**: Mobile-friendly dengan grid system
- **Komponen UI**: Product cards, navbar, buttons dengan hover effects
- **Animasi**: Smooth transitions, loading states, notifications
- **Color Scheme**: Tema denim (hitam, putih, abu-abu)

### Fitur E-Commerce
- **Katalog Produk**: List produk dengan pagination dan filtering
- **Detail Produk**: Informasi lengkap dengan image gallery
- **Keranjang Belanja**: Add/remove items, update quantities
- **Checkout Process**: Form pengiriman lengkap
- **Pembayaran QRIS**: QR code generation dan upload bukti
- **Search & Filter**: Pencarian produk dan filter kategori
- **Best Seller Badge**: Highlight produk populer

## Teknologi yang Digunakan

- **Backend**: Django 4.2.7
- **Frontend**: Tailwind CSS (CDN)
- **Database**: SQLite (development)
- **Image Processing**: Pillow
- **QR Code**: qrcode library
- **Icons**: Font Awesome 6.4.0

## Struktur Project

```
denim/
|-- manage.py
|-- denim/                 # Django project settings
|   |-- __init__.py
|   |-- settings.py         # Konfigurasi Django
|   |-- urls.py            # URL routing utama
|   |-- wsgi.py
|   |-- asgi.py
|-- toko/                  # Django app
|   |-- __init__.py
|   |-- admin.py           # Admin panel configuration
|   |-- apps.py
|   |-- models.py          # Database models
|   |-- views.py           # View functions
|   |-- urls.py            # App URL routing
|   |-- static/            # Static files
|   |-- templates/         # HTML templates
|   |   |-- toko/
|   |   |   |-- base.html      # Base template
|   |   |   |-- home.html      # Homepage
|   |   |   |-- detail.html    # Product detail
|   |   |   |-- cart.html      # Shopping cart
|   |   |   |-- checkout.html  # Checkout process
|   |   |   |-- pembayaran.html # Payment page
|   |   |   |-- search.html    # Search results
|   |   |   |-- kategori.html  # Category filter
|   |-- migrations/        # Database migrations
|-- media/                 # User uploaded files
|   |-- produk/           # Product images
|   |-- qrcode/           # QR code images
|   |-- bukti/            # Payment proofs
|-- static/               # Static files
|-- db.sqlite3           # SQLite database
|-- requirements.txt      # Python dependencies
```

## Instalasi & Setup

### 1. Clone Repository
```bash
git clone <repository-url>
cd denim
```

### 2. Setup Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 6. Run Development Server
```bash
python manage.py runserver
```

Buka browser dan akses `http://127.0.0.1:8000`

## Admin Panel

Akses admin panel di `http://127.0.0.1:8000/admin` dengan credentials superuser yang Anda buat.

### Fitur Admin:
- **Manajemen Produk**: Tambah/edit produk dengan image preview
- **Manajemen Pesanan**: Monitor status pesanan dan pembayaran
- **Filtering & Search**: Cari produk/pesanan dengan mudah
- **QR Code Preview**: Lihat QR code yang di-generate otomatis

## Cara Penggunaan

### 1. Menambah Produk
1. Login ke admin panel
2. Pilih "Produk" > "Add"
3. Isi informasi produk (nama, harga, deskripsi, stok, kategori)
4. Upload gambar produk
5. Set "Best Seller" jika produk populer
6. Tambahkan diskon jika ada promo

### 2. Proses Belanja Customer
1. Customer browse produk di homepage
2. Klik "Detail" untuk lihat informasi lengkap
3. Klik "Tambah ke Keranjang" atau gunakan quantity selector
4. Checkout dengan mengisi informasi pengiriman
5. Scan QR code untuk pembayaran QRIS
6. Upload bukti pembayaran (opsional)

### 3. Monitoring Pesanan
1. Admin dapat melihat semua pesanan di admin panel
2. Update status pesanan (pending -> dibayar -> diproses -> dikirim -> selesai)
3. Lihat QR code dan bukti pembayaran
4. Export data jika diperlukan

## Customization

### Mengubah Warna Tema
Edit `base.html` dan ubah konfigurasi Tailwind colors:
```javascript
colors: {
    denim: {
        50: '#f8fafc',
        900: '#0f172a',
        // ... tambahkan warna custom
    }
}
```

### Menambah Kategori Produk
Edit `models.py` di `Produk.KATEGORI_CHOICES`:
```python
KATEGORI_CHOICES = [
    ('celana', 'Celana Jeans'),
    ('jaket', 'Jaket Denim'),
    ('kaos', 'Kaos Denim'),
    ('aksesoris', 'Aksesoris Denim'),
    ('kategori_baru', 'Kategori Baru'),  # Tambah kategori baru
]
```

### Integrasi Payment Gateway
Untuk integrasi dengan payment gateway real (Midtrans, Xendit):
1. Install library payment gateway
2. Update views.py di function `checkout()`
3. Ganti QR code generation dengan API payment gateway
4. Update callback URL untuk webhook

## Deployment

### Production Setup
1. Set `DEBUG = False` di settings.py
2. Configure `ALLOWED_HOSTS`
3. Setup production database (PostgreSQL/MySQL)
4. Configure static files serving
5. Setup domain dan SSL
6. Environment variables untuk sensitive data

### Environment Variables
Buat file `.env`:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=your-database-url
```

## Troubleshooting

### Common Issues

**1. Images tidak muncul**
- Pastikan `MEDIA_URL` dan `MEDIA_ROOT` sudah dikonfigurasi
- Tambahkan serving media files di development

**2. QR Code tidak ter-generate**
- Install library qrcode: `pip install qrcode`
- Pastikan folder `media/qrcode/` ada dan writable

**3. Cart tidak berfungsi**
- Pastikan session middleware aktif di settings.py
- Check browser cookies enabled

**4. Admin panel tidak muncul**
- Run `python manage.py createsuperuser`
- Check user permissions

## Contributing

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License - feel free to use for commercial or personal projects.

## Support

Untuk bantuan atau pertanyaan:
- Email: info@denimstore.com
- Phone: +62 812-3456-7890
- Documentation: [Link ke dokumentasi]

---

**Denim Store** - E-Commerce solution for modern denim retail
