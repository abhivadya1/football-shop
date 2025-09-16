# Anak Agung Ngurah Abhivadya Nandana/2406439192/PBP F

TAUTAN PWS:
https://anak-agung44-louisballton.pbp.cs.ui.ac.id/

# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step :
    Membuat direktori baru dulu bernama football-shop lalu membuat mengaktifkan venv, lalu membuat requirements.txt supaya
     bisa menginstall banyak dependencies, lalu buat proyek django baru dengan nama football_shop, setelah itu lakukan konfigurasi environment variables dan proyek, setelah selesai jalankan server dan cek di localhost,
     setelah berhasil saya push ke github. Selanjutnya buat aplikasi main dengan "python manage.py startapp main", lalu tambahkan 'main' ke dalam daftar aplikasi yang ada di settings.py pada variabel INSTALLED_APPS,
     setelah itu saya buat berkas main.html di dalam templates yang berfungsi sebagai tampilan nanti.
   # Lalu membuat model pada aplikasi main dengan nama Product:

    class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Sepatu Bola'),
        ('jersey', 'Jersey'),
        ('ball', 'Bola'),
        ('equipment', 'Peralatan Latihan'),
        ('accessories', 'Aksesoris'),
        ('other', 'Lainnya'),
    ]
   
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    #Tambahan fitur
    item_views = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)
    stock = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - Rp{self.price:,}"
    
    @property
    def is_popular(self):
        return self.item_views > 5

    def increment_views(self):
        self.item_views += 1
        self.save()

   # Setelah itu membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas:
    def show_main(request):
    context = {
        'npm' : '2406439192',
        'name': 'Anak Agung Ngurah Abhivadya Nandana',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)

   # Lalu membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py:
     app_name = 'main'
  
     urlpatterns = [
          path('', show_main, name='show_main'),
      ]

   # Melakukan deployment ke PWS:
     membuat proyek baru dengan nama "louisballton", lalu simpan Project Credentials, lalu pilih enviros dan ubah raw editor sesuai dengan .env.prod dan pastikan skemanya tugas_individu, lalu
     tambahkan URL deployment PWS pada ALLOWED_HOSTS setelah itu git add commit dan push ke github, lalu jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS dan masukan usn pw yang tadi
     disimpan diawal.

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html :
<img width="1104" height="637" alt="image" src="https://github.com/user-attachments/assets/1b0cfa1a-3bf5-4973-9ebf-85b2ffe52487" />

    1. HTTP Request :
        Browser (client) mengirim permintaan ke server Django.
    
    2. URLs (urls.py) :
        Django pertama kali mengecek urls.py.
        Tugasnya mencocokkan URL request dengan pola yang ada.
        Kalau cocok, request diteruskan ke fungsi yang sesuai di views.py.

    3. Views (views.py) :
        Bagian ini adalah "otak" aplikasi.
        View menerima request dari urls.py, lalu menentukan:
          Apakah perlu ambil data dari model?
          Apakah perlu langsung kirim response (misalnya teks/JSON)?
          Atau perlu render template HTML?

    4. Models (models.py) + Database :
        Jika view butuh data, dia akan memanggil model.
        Model adalah representasi tabel database dalam bentuk Python class.
        View bisa read/write data lewat model.
        Django ORM yang akan berkomunikasi dengan database.

    5. Template (.html) :
        Setelah dapat data dari model, view akan me-render template.
        Template adalah file HTML yang bisa diberi placeholder untuk data dari view.

    6. HTTP Response
        Template yang sudah diisi data dikirim balik sebagai HTML ke client.
        Browser menampilkan halaman jadi yang sudah berisi data produk.

    Ringkasan:
    Request → masuk ke urls.py
    urls.py → arahkan ke views.py
    views.py → ambil data dari models.py (DB) & pilih template
    template HTML → di-render dengan data
    Response → dikirim ke client

  # 3. Jelaskan peran settings.py dalam proyek Django!
    settings.py itu ibarat buku panduan atau pusat pengaturan dari sebuah proyek Django. Semua konfigurasi penting yang menentukan bagaimana aplikasi jalan, ditaruh di situ.
    Singkatnya, tanpa settings.py, Django nggak akan tahu harus jalan dengan aturan apa. File ini yang bikin proyek kita bisa dibedakan antara mode pengembangan (development) dan mode produksi (production).

  # 4. Bagaimana cara kerja migrasi database di Django?
    makemigrations = bikin blueprint perubahan (file migrasi).
    migrate = jalankan blueprint itu ke database.
    Dengan sistem ini, kita nggak perlu menulis SQL manual tiap kali ubah model, cukup ubah models.py lalu migrasi.

  # 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Django sering dijadikan permulaan belajar pengembangan perangkat lunak karena framework ini sudah lengkap dan terstruktur. Banyak fitur penting seperti autentikasi, manajemen database, dan keamanan dasar sudah tersedia,
    sehingga pemula bisa langsung fokus memahami alur kerja aplikasi. Pola kerja model, view, dan template juga memudahkan dalam membangun aplikasi secara rapi. Ditambah dengan dokumentasi yang jelas, komunitas besar,
    serta penggunaan bahasa Python yang sederhana, itu sebabnya Django menjadi pilihan tepat untuk memahami dasar pengembangan perangkat lunak.

  # 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Menurut saya tutorialnya sudah baik karena mudah dipahami, terlebih untuk pemula seperti saya.
