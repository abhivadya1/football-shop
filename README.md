# Anak Agung Ngurah Abhivadya Nandana/2406439192/PBP F

TAUTAN PWS:
https://anak-agung44-louisballton.pbp.cs.ui.ac.id/

<details>
<Summary><b><Tugas2></b></Summary>
    
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
</details>

<details>
<Summary><b><Tugas3></b></Summary>
    
# TUGAS 3
# 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery diperlukan dalam implementasi platform karena ia yang memastikan informasi bisa berpindah dari server ke pengguna, antar komponen sistem, dan antar layanan eksternal secara aman, cepat, dan         konsisten. Tanpa mekanisme ini, platform hanya jadi sistem statis yang tidak bisa benar-benar digunakan.
# 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya, JSON lebih baik dibandingkan XML karena lebih ringkas, mudah dibaca, cepat diproses, dan langsung terintegrasi dengan JavaScript sehingga sangat cocok untuk web development modern. XML masih        berguna di sistem lama atau kebutuhan khusus, tetapi JSON lebih populer karena lebih sederhana dan efisien untuk pertukaran data di API masa kini.
# 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Menurut saya, fungsi dari method is_valid() pada form Django adalah memeriksa apakah data yang dikirim melalui form sesuai dengan aturan validasi yang sudah ditentukan di forms.py maupun di model.
    Kenapa kita butuh is_valid()?
    Karena tanpa validasi, data yang tidak sesuai bisa masuk ke database, misalnya email salah format, harga kosong, atau kategori tidak valid. Dengan is_valid(), kita bisa pastikan hanya data yang benar dan         bersih yang tersimpan.
# 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    csrf_token di Django berfungsi mencegah serangan CSRF dengan memberi token unik pada setiap form. Tanpa token ini, penyerang bisa memalsukan request (misalnya transfer uang atau ganti password) dengan            memanfaatkan session user yang masih aktif.
# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.
    1. Awalnya saya menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
        def show_xml(request):
            product_list = Product.objects.all()
            xml_data = serializers.serialize("xml", product_list)
            return HttpResponse(xml_data, content_type="application/xml")
    
        def show_json(request):
            product_list = Product.objects.all()
            json_data = serializers.serialize("json", product_list)
            return HttpResponse(json_data, content_type="application/json")
        
        def show_xml_by_id(request, product_id):
            try:
                product_list = Product.objects.filter(pk=product_id)
                xml_data = serializers.serialize("xml", product_list)
                return HttpResponse(xml_data, content_type="application/xml")
            except Product.DoesNotExist:
                return HttpResponse(status=404)
        
        def show_json_by_id(request, product_id):
            try:
                product_list = Product.objects.get(pk=product_id)
                json_data = serializers.serialize("json", [product_list])
                return HttpResponse(json_data, content_type="application/json")
            except Product.DoesNotExist:
                return HttpResponse(status=404)
        lalu di tambahkan ke dalam urls.py
    2. Lalu saya membuat direktori baru di direktori utama dengan nama templates yang berisi file base.html, base.html berfungsi sebagai template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya di dalam proyek.
    3. Lalu saya update settings.py yang berisi TEMPLATES dan menambahkan 'DIRS': [BASE_DIR / 'templates'] agar file base.html terdeteksi sebagai file templates
    4. Buat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data Product baru. 
    5. Buka berkas views.py yang ada pada direktori main dan tambahkan beberapa import lalu menambahkan fungsi fungsi berikut:
        def create_product(request):
            form = ProductForm(request.POST or None)
        
            if form.is_valid() and request.method == "POST":
                form.save()
                return redirect('main:show_main')
        
            context = {'form': form}
            return render(request, "create_product.html", context)

        def show_product(request, id):
            product = get_object_or_404(Product, pk=id)
            product.increment_views()
        
            context = {
                'product': product
            }
        
            return render(request, "product_detail.html", context)
    6. Buka urls.py yang ada pada direktori main lalu import fungsi fungsi yang tadi ditambahkan:
            urlpatterns = [
        path('', show_main, name='show_main'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
        path('create-product/', create_product, name='create_product'),
        path('product/<str:id>/', show_product, name='show_product'),
    ]
# 6. Screenshot Localhost xml, json, xml by id, json by id.
Localhost xml
<img width="1919" height="615" alt="image" src="https://github.com/user-attachments/assets/c0349d55-7934-4369-80bf-156f14492708" />
Localhost json
<img width="1919" height="707" alt="image" src="https://github.com/user-attachments/assets/cd89f794-c9c1-4578-831b-c021e3356fb6" />
Localhost xml by id
<img width="1919" height="444" alt="image" src="https://github.com/user-attachments/assets/c2ce1334-8eda-4e25-914a-b9053a277b42" />
Localhost json by id
<img width="1919" height="508" alt="image" src="https://github.com/user-attachments/assets/58aca142-b005-4351-97fb-dcf77c9de258" />
</details>


<details>
<Summary><b><Tugas4></b></Summary>
    
# TUGAS 4
# 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    AuthenticationForm adalah form bawaan Django (dari django.contrib.auth.forms) yang digunakan untuk proses login pengguna.
    Form ini menyediakan field username dan password, serta sudah otomatis memvalidasi kredensial dengan sistem autentikasi Django.

    Kelebihan:
    Praktis → bisa langsung dipakai untuk login tanpa harus membuat form manual.
    Aman → sudah terintegrasi dengan hashing password dan validasi bawaan Django.
    Terintegrasi → bekerja langsung dengan authenticate() dan login() Django.

    Kekurangan:
    Hanya mendukung login berbasis username & password secara default.
    Kurang fleksibel untuk kasus login custom (misalnya login pakai email, OTP, atau social login) → perlu di-extend.

# 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    Autentikasi (Authentication): proses memverifikasi identitas pengguna (apakah dia benar pengguna yang terdaftar?).
    ➝ Contoh: login dengan username & password.
    Otorisasi (Authorization): proses menentukan hak akses pengguna setelah identitasnya terverifikasi.
    ➝ Contoh: hanya admin boleh menghapus data, user biasa hanya bisa melihat.

    Autentikasi:
    authenticate() → cek kredensial.
    login() → menyimpan status login di session.
    request.user.is_authenticated → cek apakah user sedang login.
    
    Otorisasi:
    Properti user: is_staff, is_superuser.
    Sistem permissions dan groups.
    Decorator: @login_required, @permission_required, @user_passes_test.

# 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Session
    Kelebihan:
    Data disimpan di server → lebih aman.    
    Bisa menyimpan data kompleks (dictionary, objek serializable).
    Terintegrasi dengan Django (SessionMiddleware).  
    
    Kekurangan:
    Membebani server (butuh storage per-user).
    Jika aplikasi berskala besar → butuh Redis/DB cluster untuk menyimpan session.

    
    Cookies
    Kelebihan:
    Disimpan di sisi client → tidak membebani server.
    Cocok untuk data ringan (misalnya preferensi bahasa, tema).
    Bisa langsung dibaca oleh JavaScript.

    Kekurangan:
    Ukuran terbatas (sekitar 4KB per cookie).
    Rentan dicuri jika ada serangan XSS atau session hijacking.
    Bisa dihapus oleh pengguna kapan saja.

# 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Tidak 100% aman. Ada risiko:
    XSS (Cross-Site Scripting): script berbahaya bisa mencuri cookie.
    Session Hijacking: jika session ID dalam cookie dicuri.
    CSRF (Cross-Site Request Forgery): cookie bisa dipakai dalam request palsu.
    
    Bagaimana Django menangani hal ini?
    HttpOnly=True → mencegah cookie diakses lewat JavaScript.
    Secure=True → cookie hanya dikirim via HTTPS.
    SESSION_COOKIE_AGE → atur masa berlaku cookie.
    CSRF_COOKIE_SECURE + CsrfViewMiddleware → mencegah CSRF.
    Signed cookies (SignedCookieSession) → Django menandatangani cookie sehingga tidak bisa dimodifikasi sembarangan.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).


</details>
