# IMPLEMENTASI-PEMROGRAMAN-SOKET-CLIENT-SERVER-PYTHON-TCP-UDP-# 
PROGRAM SOCKET CLIENT–SERVER PYTHON (TCP)

**Tugas 11 – Jaringan Komputer (IF25-21008)**  
Program Studi Teknik Informatika – Institut Teknologi Sumatera (ITERA)

## Identitas Mahasiswa

- **Nama:** Sena Permatasari
- **NIM:** 124140018
- **Kelas:** RA
- **Mata Kuliah:** Jaringan Komputer
- **Dosen Pengampu:** Hartanto Tantriawan, S.Kom., M.Kom.

## Deskripsi Proyek

Program ini merupakan implementasi komunikasi jaringan menggunakan arsitektur **Client–Server** dengan bahasa pemrograman Python 3 dan protokol TCP (Transmission Control Protocol).

Program terdiri dari dua file utama, yaitu `server.py` sebagai penerima dan pemroses pesan serta `client.py` sebagai pengirim pesan. Client dapat mengirimkan teks biasa maupun operasi matematika, kemudian server memproses permintaan dan mengirimkan hasilnya kembali kepada client.

Program juga menerapkan mekanisme timeout selama 10 detik untuk mengantisipasi keterlambatan respons server.

## Fitur Program

1. **Komunikasi Client–Server:** Menggunakan protokol TCP dengan socket SOCK_STREAM.
2. **Reverse String:** Membalik urutan karakter dari teks yang dikirimkan client.
3. **Word Count:** Menghitung jumlah kata dan karakter dalam teks.
4. **Kalkulator Aritmatika:** Melakukan operasi matematika melalui perintah `calc:`.
5. **Timeout Handling:** Menggunakan `settimeout(10.0)` untuk membatasi waktu tunggu respons.
6. **Error Handling:** Menangani kondisi server tidak aktif, koneksi terputus, dan timeout.
7. **Simulasi Timeout:** Menggunakan perintah `test_delay` untuk menguji keterlambatan respons server.

## Struktur Folder

```text
Tugas11-JaringanKomputer/
│
├── server.py
├── client.py
└── README.md
```

## Persyaratan

Sebelum menjalankan program, pastikan perangkat telah memiliki:

- Python 3.8 atau versi lebih baru.
- Terminal atau Command Prompt.
- Visual Studio Code (opsional).
- Koneksi jaringan untuk pengujian antarperangkat.

Program menggunakan modul bawaan Python, sehingga tidak memerlukan instalasi library tambahan.

## Cara Menjalankan Program

### 1. Menjalankan Server

Buka terminal pertama, kemudian masuk ke direktori folder proyek.

Jalankan perintah:

```bash
python server.py
```

Server akan aktif dan mendengarkan koneksi pada port `65432`.

### 2. Menjalankan Client

Buka terminal kedua pada direktori yang sama.

Jalankan perintah:

```bash
python client.py
```

Masukkan alamat IP server dan port yang dituju.

Untuk pengujian pada satu perangkat, gunakan konfigurasi default:

- IP Server: `127.0.0.1`
- Port: `65432`

Tekan Enter untuk menggunakan nilai default.

### 3. Mengirim Pesan

Setelah client berhasil terhubung, pengguna dapat memasukkan beberapa jenis perintah berikut.

| Input | Fungsi |
|---|---|
| `Halo ITERA` | Membalik teks dan menghitung kata serta karakter |
| `calc: 125 * 8` | Melakukan operasi perkalian |
| `calc: (200 + 50) / 5` | Melakukan operasi aritmatika campuran |
| `test_delay` | Menguji mekanisme timeout |
| `exit` | Mengakhiri koneksi client-server |

## Konfigurasi Program

| Parameter | Nilai |
|---|---|
| Protokol | TCP |
| Address Family | AF_INET (IPv4) |
| Socket Type | SOCK_STREAM |
| Server Host | 0.0.0.0 |
| Client Default Host | 127.0.0.1 |
| Port | 65432 |
| Buffer Size | 1024 bytes |
| Timeout Client | 10 detik |
| Encoding | UTF-8 |

## Pengujian Program

Pengujian dilakukan untuk memastikan komunikasi dua arah antara client dan server berjalan sesuai dengan fungsinya.

Skenario pengujian meliputi:

1. Pengujian pengiriman dan penerimaan teks biasa.
2. Pengujian pembalikan string dan perhitungan jumlah kata serta karakter.
3. Pengujian operasi kalkulator aritmatika.
4. Pengujian timeout menggunakan perintah `test_delay`.
5. Pengujian koneksi ketika server tidak aktif.
6. Pengujian komunikasi antarperangkat melalui jaringan Wi-Fi/LAN.

## Catatan

- Jalankan server terlebih dahulu sebelum menjalankan client.
- Pastikan alamat IP dan port yang dimasukkan client sesuai dengan konfigurasi server.
- Untuk pengujian antarperangkat, gunakan alamat IP lokal perangkat yang menjalankan server.
- Pastikan firewall mengizinkan koneksi masuk melalui port `65432`.
- Perintah `test_delay` menghasilkan penundaan selama 12 detik, sedangkan batas waktu tunggu client adalah 10 detik.

## Penutup

Program ini dibuat sebagai pemenuhan Tugas 11 mata kuliah Jaringan Komputer dengan tujuan memahami implementasi komunikasi socket berbasis TCP, pemrosesan pesan dua arah, serta penerapan mekanisme timeout untuk menangani blocking I/O menggunakan Python.

---

**Sena Permatasari**  
**124140018 – Teknik Informatika**  
**Institut Teknologi Sumatera (ITERA)**  
**2026**
