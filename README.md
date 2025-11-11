# 🎮 Captcha Challenge

**Captcha Challenge** adalah game interaktif berbasis *hand landmark recognition* yang menggabungkan teknologi *computer vision* dan *audio feedback*.  
Pemain diminta untuk menyusun potongan gambar seperti puzzle CAPTCHA secara real-time menggunakan gerakan tangan di depan kamera.  

Game ini dikembangkan sebagai bagian dari **Tugas Besar Multimedia**, dengan kolaborasi tiga anggota tim yang memiliki tanggung jawab berbeda pada setiap modul.

---

## 👥 **Anggota Kelompok**

| Nama | NIM (Opsional) | Jobdesk |
|------|----------------|--------|
| Asavira Azzahra | 122140067 | Sound |
| Dinda Joycehana | 122140 | Hand Landmarking |
| Hizkia C | 122140 | Camera |

---

## 🚀 **Deskripsi Singkat**

### 🎯 Tujuan
Menciptakan pengalaman interaktif di mana pengguna dapat berinteraksi langsung dengan sistem CAPTCHA menggunakan tangan mereka sendiri.  
Game ini mengombinasikan pengenalan gerakan tangan (*hand landmark recognition*), deteksi posisi puzzle, serta efek suara yang memberikan umpan balik secara real-time.

---

## ⚙️ **Fitur Utama**
- 🎥 **Kamera Real-Time** – menampilkan umpan langsung dari webcam.  
- ✋ **Deteksi Tangan (MediaPipe Hands)** – mengenali gesture tangan, termasuk pinch (🤏🏻).  
- 🧩 **Puzzle CAPTCHA Interaktif** – potongan gambar dapat dipindahkan dan disusun ulang.  
- 🔊 **Efek Suara Interaktif** – setiap gerakan dan keberhasilan memberikan umpan balik suara “klik” dan “cling”.  

---

## 🧰 **Teknologi yang Digunakan**
| Library | Fungsi |
|----------|---------|
| **OpenCV** | Menangkap dan memproses gambar dari kamera. |
| **MediaPipe Hands** | Mendeteksi posisi jari dan gesture tangan. |
| **Pygame** | Mengatur dan memutar efek suara. |
| **Python 3.x** | Bahasa utama untuk logika dan integrasi antar modul. |

---

## 🧩 **Struktur Proyek**

