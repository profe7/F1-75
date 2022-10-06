# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

# Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
1. Kegunaaan CSRF token (Cross-Site Request Forgery Token) pada elemen form adalah untuk menyediakan sebuah token acak aman yang bersifat unik untuk setiap sesi user. Token ini diperlukan untuk menangkal serangan CSRF yang memanfaatkan status user yang telah terotentikasi untuk melakukan aksi dalam aplikasi secara involunter. Bahaya dari kondisi ini sudah jelas, seorang penyerang dapat menggunakan serangan CSRF untuk mengubah kredensial kritis seperti password milik pengguna.

# Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
2.  Bisa, elemen <form> dapat dibuat secara manual, karena pada kodratnya <form> adalah sebuah wrapper untuk beberapa field `<input>`. Saya mengaplikasikan hal ini dalam pembuatan file HTML update saya.

# Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

3. Saat pengguna memencet elemen tombol submit dalam aplikasi browser akan mengirim sebuah request POST dengan input yang telah dimasukan user. Request tersebut kemudian akan diproses oleh fungsi-fungsi yang terdapat dalam views.py, apabila valid maka data tersebut akan disimpan di database, apabia tidak, maka akan ditampilkan pesan error sesuai error yang terjadi Setelah itu akan ada respon HTTP redirect untuk menampilkan data tersebut

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

### STEP 1 = Buat aplikasi baru bernama todolist
### STEP 2 = Tambahkan aplikasi tersebut ke settings.py di project_django
### STEP 3 = Tambahkan urlpatterns yang sesuai pada urls.py project_django
### STEP 4 = Buat model Task dengan field yang sesuai spesifikasi soal
### STEP 5 = Menambahkan fungsi-fungsi yang relevan di views.py todolist, ada beberapa fungsi yang hanya bisa diakses dengan login sebagai user (buat task, delete task, update task, logout) ada juga yang tidak (login, register) serta membuat forms.py untuk mengkomplemen fungsi yang terdapat di views.py
### STEP 6 = Impelementasi routings di urls.py milik todolist
### STEP 7 = Membuat file HTML sesuai fungsi yang ingin diimplementasikan
### STEP 8 = Testing, finishing, etc.
### STEP 9 = Push to repo dan deploy ke heroku

#   Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

4. Inline CSS menaruh style attribute didalam elemen HTML, Internal CSS menaruh elemen `<style>` dalam bagian head file HTML, External CSS menaruh elemen `<link>` dalam bagian head HTML.

Kelebihan Internal = Memastikan semua elemen didalam halaman seragam.
Kekurangan Internal = Scope hanya satu halaman, file HTML berantakan.

Kelebihan Inline = Bisa digunakan bersamaan dengan internal, styling lebih presisi daripada internal.
Kekurangan Inline = Memakan waktu banyak untuk styling secara presisi, file HTML berantakan.

Kelebihan Eksternal = Desain yang koheren untuk satu website.
Kekurangan Eksternal = Tidak bisa mengontrol elemen secara spesifik.

# Jelaskan tag HTML5 yang kamu ketahui.

5. `<style>` untuk informasi styling CSS. `<center>` untuk menengahkan elemen. `<div>` untuk mengkompartemen elemen. `<td>`sel tabel. `<tr>` baris tabel. `<a>` hyperlink. `<h>` header. `<a>` hyperlink. Dst...

#  Jelaskan tipe-tipe CSS selector yang kamu ketahui.

6. Class selector untuk menselect elemen HTML dengan atribut class tertentu. Element selector untuk menselect elemen HTML sesuai nama elemen tersebut. ID selector untuk menselect elemen berdasarkan atribut ID sebuah elemen HTML. Universal selector untuk menselect semua elemen HTML. Grouping selector untuk menselect semua elemen HTML dengan definisi style yang sama.

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

### STEP 1 = Install boostrap melalui CDN yang disediakan di Lab 4.
### STEP 2 = Styling internal dalam file HTML.
### STEP 3 = Menggunakan unit % atau unit lain yang tidak fixed untuk mengimplementasikan responsiveness.
### STEP 4 = Menambahkan kode untuk fitur hover pada card.

# Link to app
https://djangolab2.herokuapp.com/todolist/