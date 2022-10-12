# Tugas 6: Implementasi AJAX GET & POST

# Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

1. Perbedaan antara synchronous dan asynchronous programming adalah, pada syncrhonous programming, kode berjalan secara sekuensial, untuk setiap operasi harus menunggu operasi sebelumnya untuk selesai sebelum mengeksekusi operasi sebelumnya. Programming asynchronous berjalan secara paralel yang berarti sebuah operasi lain bisa berjalan walaupun ada operasi lain yang sedang diproses.

# Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

2. Paradigma event driven programming adalah sebuah paradigma yang berkonsep alur dari sebuah program dipengaruhi oleh action atau event yang dihasilkan oleh user. Contoh paling sederhana dari konsep ini adalah mengklik tombol submit form, saat ada aksi klik maka alur program akan berubah.

# Jelaskan penerapan asynchronous programming pada AJAX.

3. Penerapan asynchronous programming AJAX ada penerapannya dalam tugas ini, yakni mengupdate cards yang tertampil di homepage tanpa harus mereload homepage tersebut. Hal ini dicapai dengan mengambil data dari database dengan paradigma asynchronous.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

### STEP-1 = Buat view baru di views.py (show_json)
### STEP-2 = Tambahkan path baru di urls.py untuk mengakses view tersebut
### STEP-3 = Buat fungsi getJson() untuk fetch data dari database dan mengembalikannya sebagai JSON dengan AJAX GET
### STEP-4 = Buat fungsi createCards() untuk mapping data JSON tersebut menjadi cards untuk ditampilkan di homepage
### STEP-5 = Buat container dalam bentuk table di body HTML untuk menyimpan cards yang telah dibuat
### STEP-6 = Buat view baru di views.py (add_task)
### STEP-7 = Tambahkan path baru di urls.py untuk mengakses view tersebut
### STEP-8 = Handle form submitting dengan AJAX POST
### STEP-9 = Finsihing etc...

