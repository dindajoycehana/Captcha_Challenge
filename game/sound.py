import os
import pygame

#  Inisialisasi pygame mixer
pygame.mixer.init()


#  Path folder sounds harus relative terhadap file ini
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_DIR = os.path.join(BASE_DIR, "assets", "sounds")

# File sound
CLICK_PATH = os.path.join(SOUND_DIR, "click.wav")
WIN_PATH   = os.path.join(SOUND_DIR, "win.wav")


#  Load audio dengan pengecekan aman
def load_sound(path):
    if not os.path.exists(path):
        print(f"[WARNING] File sound tidak ditemukan: {path}")
        return None
    return pygame.mixer.Sound(path)

click_sound = load_sound(CLICK_PATH)
win_sound   = load_sound(WIN_PATH)


#  Fungsi bermain sound
def play_click_sound():
    """Mainkan suara klik ketika swap puzzle"""
    if click_sound:
        click_sound.set_volume(1.0)
        click_sound.play()


def play_win_sound():
    """Mainkan suara saat puzzle selesai"""
    if win_sound:
        win_sound.set_volume(0.6)
        win_sound.play()


#  Test manual (jika file ini dijalankan sendiri)
if __name__ == "__main__":
    print("Testing sounds...")

    print("Play click sound...")
    play_click_sound()
    pygame.time.wait(1200)

    print("Play win sound...")
    play_win_sound()
    pygame.time.wait(2000)

    print("Done.")

