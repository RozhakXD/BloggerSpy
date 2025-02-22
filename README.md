# BloggerSpy - Extract, Analyze, and Monitor Blogger Data
![BloggerSpy - Logo](https://github.com/user-attachments/assets/64cfba76-7486-4a60-864b-0412e919c902)
![BloggerSpy](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

BloggerSpy adalah sebuah alat berbasis Python yang memanfaatkan **Google Dork** untuk mengumpulkan dan mengekstrak informasi dari profil pengguna **Blogger**. Alat ini memungkinkan pengumpulan data seperti nama, email (jika tersedia), tanggal pembuatan akun, jumlah tampilan profil, dan informasi lainnya secara otomatis.

## ✨ Fitur
✅ Menggunakan **Google Dork** untuk mencari profil Blogger secara otomatis.  
✅ Mengambil informasi seperti **nama pengguna, email, tanggal bergabung, jumlah tampilan profil**.  
✅ Menampilkan data dalam format yang rapi dan mudah dibaca.  
✅ Menyimpan hasil ekstraksi ke dalam file **.txt** untuk referensi lebih lanjut.  
✅ Berjalan di **Windows, Linux, dan macOS** dengan dependensi minimal.  

## 🚀 Instalasi
```bash
$ apt update -y && apt upgrade -y
$ pkg install git python-pip
$ git clone https://github.com/RozhakXD/BloggerSpy.git
$ cd "BloggerSpy"
$ pip install -r requirements.txt
$ python Run.py
```

## 📂 Output Data

Hasil scraping akan tersimpan dalam file **Temporary/Results.txt** dalam format berikut:
```
Nama Lengkap | Profil Blogger | Tanggal Bergabung | Tampilan Profil | Email
John Doe | https://www.blogger.com/profile/123456 | Januari 2020 | 500 | johndoe@gmail.com
Jane Smith | https://www.blogger.com/profile/789012 | Maret 2018 | 1200 | Tidak ditemukan
```

## 🖼️ Tangkapan Layar
![FunPic_20250222](https://github.com/user-attachments/assets/d81d121f-9db2-4092-a23f-d6d5e36ec644)

## 💖 Dukungan
Dukung proyek ini melalui [Paypal](https://paypal.me/rozhak9), [Saweria](https://saweria.co/rozhak09), atau [Trakteer](https://trakteer.id/rozhak_official/tip). Terima kasih atas dukungan Anda! ❤️

## ⚠️ Disclaimer
**BloggerSpy** dibuat untuk tujuan edukasi dan penelitian. Penggunaan alat ini untuk tujuan ilegal, seperti scraping tanpa izin, bisa melanggar **Terms of Service** dari Google dan Blogger. Gunakan dengan bijak dan hanya untuk keperluan yang diperbolehkan.

## 🛠 Kontribusi
Kontribusi sangat diterima! Jika Anda memiliki ide perbaikan atau fitur baru, silakan buat **pull request** atau buka **issue** di repository.

## 📜 Lisensi
BloggerSpy dirilis di bawah lisensi **MIT License**. Silakan lihat file `LICENSE` untuk detail lebih lanjut.
