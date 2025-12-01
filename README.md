# 🎮 Captcha Challenge — Live Glass Puzzle Game

**Captcha Challenge** adalah permainan puzzle interaktif berbasis *hand tracking* yang memanfaatkan teknologi *computer vision*, *glass overlay system*, dan *gesture-based interaction*.  
Pemain harus menyusun kembali potongan tampilan webcam yang dipecah menjadi blok-blok “kaca” hingga membentuk gambar live yang utuh.

Project ini dikembangkan sebagai bagian dari **Tugas Besar Multimedia**.

---

## 👥 Anggota Kelompok

| Nama              | NIM        |
|-------------------|------------|
| Dinda Joycehana   | 122140048  |
| Hizkia C          | 122140110  |
| Asavira Azzahra   | 122140067  |

---

## 🚀 Deskripsi Singkat

Pada versi terbaru, **Captcha Challenge** menggunakan sistem *Live Glass Puzzle*,  
di mana tampilan webcam **dibagi menjadi beberapa glass blocks**.  
Hand Tracking digunakan untuk:

- mengambil blok kaca dengan gesture **pinch (🤏🏻)**
- menukar posisi dua blok
- menyusun ulang hingga membentuk gambar webcam yang benar

📌 **Catatan:**  
Nama project **tetap "Captcha Challenge"**, meskipun puzzle yang disusun adalah **grid dari glass overlay**, bukan grid landmark tangan.  
Landmark hanya digunakan untuk gesture namun *ditutup (overlay)* oleh kaca puzzle agar tampilan lebih bersih.

---

## 🎮 Cara Bermain

1. Jalankan program  
2. Tekan **SPACE** untuk memulai permainan  
3. Gunakan gesture **pinch** (ibu jari + telunjuk) untuk mengambil blok  
4. Pindahkan tangan ke blok lain sambil pinch  
5. Lepaskan pinch untuk **menukar posisi dua blok**  
6. Susun semua blok hingga gambar kembali utuh  
7. Tekan **R** untuk reset  
8. Tekan **Q** untuk keluar  

---

## 🛠 Instalasi

### Prasyarat
- Python 3.8 atau lebih baru  
- Webcam aktif  
- OS Windows / macOS / Linux  

### Langkah Instalasi

1. Clone repository:
   ```bash
   git clone <link-repo-kalian>
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
3. Menjalankan Game:
    ```bash
    python main.py


## 🧩 **Struktur Proyek**
- Menjalankan Game:
    ```bash
    Captcha_Challenge/
    │
    ├── main.py                 # Entry point utama
    ├── README.md               # Dokumentasi proyek'
    ├── requirements.txt        # Dependencies
    │
    └── game/                   # Package inti game
    ├── __init__.py
    ├── puzzle.py           # Logika game & game loop
    ├── hand_tracker.py     # Tracking tangan dengan MediaPipe
    ├── puzzle_pieces.py    # Pengaturan potongan puzzle
    └── game_renderer.py    # Renderer visual
    

## 🧩 **Fitur Utama**
✋ Hand Tracking real-time (MediaPipe)
🤏 Gesture pinch untuk mengambil & menukar blok
🪟 Puzzle dari tampilan webcam live
🔢 Counter pergerakan
🟩 Highlight blok yang sudah benar
🏆 Layar kemenangan saat puzzle tersusun
🔄 Reset & replay

## 🔧 **Teknologi yang Digunakan**
- OpenCV → Video capture & manipulasi frame
- MediaPipe Hands → Hand tracking + gesture detection
- NumPy → Operasi array
- Pygame → Efek suara (klik & menang)

## ⚙ **Kustomisasi**
- Atur ukuran grid puzzle di ```main.py```:
    ```bash
    puzzle = LiveGlassPuzzle(grid_size=3)
Pilihan:
- 3 → Puzzle 3x3 (9 pieces) – Default
- 4 → Puzzle 4x4 (16 pieces)
- 5 → Puzzle 5x5 (25 pieces)

## 🐛 **Troubleshooting**
Clone repository:
- Pastikan webcam tidak digunakan aplikasi lain
- Cek permission webcam pada Python

Hand tracking kurang akurat
- Pencahayaan kurang
- Jarak ideal: 30–50 cm
- Pastikan tangan terlihat jelas seluruhnya


- **Error instalasi dependencies**
    ```bash
    puzzle = LiveGlassPuzzle(grid_size=3)

## 👨‍💻 Kontribusi

Kontribusi sangat diterima!
Silakan buat Pull Request atau laporkan bug melalui Issues.

## 📝 License

Proyek ini dibuat untuk tujuan edukasi dan hiburan dalam rangka Tugas Besar Multimedia.

# 🎉 Selamat bermain Captcha Challenge — Live Glass Puzzle Game!

