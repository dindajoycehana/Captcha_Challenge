# 🪟 Live Glass Puzzle Game

Game puzzle interaktif yang menggunakan webcam dan **Hand Tracking** untuk mengatur ulang potongan-potongan "kaca" yang menampilkan bagian berbeda dari video webcam secara *live*.

> **Tugas Besar Multimedia**

## 👥 Anggota Kelompok

| Nama | NIM | Jobdesk |
| :--- | :--- | :--- |
| **Asavira Azzahra** | 122140067 | Sound & Audio Integration |
| **Dinda Joycehana** | 122140048 | Hand Landmarking (MediaPipe Hands) |
| **Hizkia Christovita Siahaan** | 122140110 | Camera Module |

---

## 📋 Deskripsi

**Live Glass Puzzle** adalah permainan puzzle unik di mana pemain harus mengatur ulang blok-blok kaca yang masing-masing menampilkan bagian berbeda dari webcam.

Pemain menggunakan gesture **pinch** (🤏) untuk mengambil sebuah blok, memindahkannya, lalu menukar posisi dua blok hingga membentuk tampilan webcam yang benar.

## 🎯 Fitur

- ✅ **Hand tracking real-time** menggunakan MediaPipe
- ✅ **Gesture pinch** untuk interaksi
- ✅ **Puzzle dari live webcam feed**
- ✅ **Counter** jumlah gerakan
- ✅ **Border hijau** untuk indikator posisi yang benar
- ✅ **Layar kemenangan** (victory overlay)
- ✅ **Efek suara** klik & kemenangan
- ✅ **Reset dan ulangi** permainan kapan saja

## 🎮 Cara Bermain

1. Jalankan program dan tekan **`SPACE`** untuk memulai permainan.
2. Gunakan gesture **pinch** (ibu jari + telunjuk) untuk mengambil satu blok kaca.
3. Geser tangan sambil tetap *pinch* untuk memindahkan blok.
4. Lepaskan *pinch* untuk menukar posisi dua blok.
5. Susun semua blok hingga membentuk tampilan webcam yang utuh.
6. Tekan **`R`** untuk mengulang permainan.
7. Tekan **`Q`** untuk keluar.

## 🛠 Instalasi

### Prerequisites
- Python 3.8+
- Webcam aktif
- OS: Windows, macOS, atau Linux

### Langkah Instalasi

1. **Clone repository:**
   ```bash
   git clone <repository-url>
   cd live-glass-puzzle

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt`

🚀 Menjalankan Game :
```python main.py```

📁 Struktur Proyek

    live-glass-puzzle/
    │
    ├── main.py                # Entry point aplikasi
    ├── requirements.txt       # Dependencies
    ├── README.md              # Dokumentasi
    │
    └── game/                  # Package utama
        ├── __init__.py        # Inisialisasi package + test audio
        ├── puzzle.py          # Game logic & game loop
        ├── hand_tracker.py    # Hand tracking (MediaPipe)
        ├── puzzle_pieces.py   # Struktur dan logika puzzle pieces
        ├── game_renderer.py   # Rendering visual puzzle
        └── sound.py           # Modul suara (klik & kemenangan)
    

🔧 Teknologi yang Digunakan
- OpenCV — menangkap & memproses video webcam
- MediaPipe — hand landmarking dan gesture recognition
- NumPy — operasi array
- Pygame — efek suara & audio feedback

Markdown

# 🪟 Live Glass Puzzle Game

Game puzzle interaktif yang menggunakan webcam dan **Hand Tracking** untuk mengatur ulang potongan-potongan "kaca" yang menampilkan bagian berbeda dari video webcam secara *live*.

> **Tugas Besar Multimedia**

## 👥 Anggota Kelompok

| Nama | NIM | Jobdesk |
| :--- | :--- | :--- |
| **Asavira Azzahra** | 122140067 | Sound & Audio Integration |
| **Dinda Joycehana** | 122140048 | Hand Landmarking (MediaPipe Hands) |
| **Hizkia Christovita Siahaan** | 122140110 | Camera Module |

---

## 📋 Deskripsi

**Live Glass Puzzle** adalah permainan puzzle unik di mana pemain harus mengatur ulang blok-blok kaca yang masing-masing menampilkan bagian berbeda dari webcam.

Pemain menggunakan gesture **pinch** (🤏) untuk mengambil sebuah blok, memindahkannya, lalu menukar posisi dua blok hingga membentuk tampilan webcam yang benar.

## 🎯 Fitur

- ✅ **Hand tracking real-time** menggunakan MediaPipe
- ✅ **Gesture pinch** untuk interaksi
- ✅ **Puzzle dari live webcam feed**
- ✅ **Counter** jumlah gerakan
- ✅ **Border hijau** untuk indikator posisi yang benar
- ✅ **Layar kemenangan** (victory overlay)
- ✅ **Efek suara** klik & kemenangan
- ✅ **Reset dan ulangi** permainan kapan saja

## 🎮 Cara Bermain

1. Jalankan program dan tekan **`SPACE`** untuk memulai permainan.
2. Gunakan gesture **pinch** (ibu jari + telunjuk) untuk mengambil satu blok kaca.
3. Geser tangan sambil tetap *pinch* untuk memindahkan blok.
4. Lepaskan *pinch* untuk menukar posisi dua blok.
5. Susun semua blok hingga membentuk tampilan webcam yang utuh.
6. Tekan **`R`** untuk mengulang permainan.
7. Tekan **`Q`** untuk keluar.

## 🛠 Instalasi

### Prerequisites
- Python 3.8+
- Webcam aktif
- OS: Windows, macOS, atau Linux

### Langkah Instalasi

1. **Clone repository:**
   ```bash
   git clone <repository-url>
   cd live-glass-puzzle
2. **Install dependencies:**
```pip install -r requirements.txt```

## 🚀 Menjalankan Game
```python main.py```

## 📁 Struktur Proyek

<pre>
live-glass-puzzle/
│
├── main.py                # Entry point aplikasi
├── requirements.txt       # Dependencies
├── README.md              # Dokumentasi
│
└── game/                  # Package utama
    ├── __init__.py        # Inisialisasi package + test audio
    ├── puzzle.py          # Game logic & game loop
    ├── hand_tracker.py    # Hand tracking (MediaPipe)
    ├── puzzle_pieces.py   # Struktur dan logika puzzle pieces
    ├── game_renderer.py   # Rendering visual puzzle
    └── sound.py           # Modul suara (klik & kemenangan)
</pre>


## 🔧 Teknologi yang Digunakan
- OpenCV — menangkap & memproses video webcam
- MediaPipe — hand landmarking dan gesture recognition
- NumPy — operasi array
- Pygame — efek suara & audio feedback

## ⚙ Kustomisasi
Ubah ukuran grid puzzle di ```main.py``` atau ```puzzle.py```:
    ```puzzle = LiveGlassPuzzle(grid_size=3)```

Pilihan level:
- grid_size=3 → 3×3 (default, mudah)
- grid_size=4 → 4×4 (sedang)
- grid_size=5 → 5×5 (sulit)

## 🐛 Troubleshooting
**Webcam tidak terdeteksi**
- Tutup aplikasi lain yang menggunakan webcam
- Berikan permission webcam pada Python/Terminal
- Restart VSCode atau interpreter

**Hand tracking tidak akurat**
- Pencahayaan cukup
- Tangan 30–50 cm dari webcam
- Background tidak gelap

**Error instalasi dependencies**
- ```pip install --upgrade pip```
- ```pip install -r requirements.txt```

## 📝 License
Project ini dibuat untuk tujuan edukasi dan demonstrasi tugas kuliah.

# Selamat bermain! 🎮✨