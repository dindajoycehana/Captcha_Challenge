import pygame
pygame.mixer.init()

click_sound = pygame.mixer.Sound("assets/sounds/click.wav")
win_sound = pygame.mixer.Sound("assets/sounds/win.wav")

def play_click_sound():
    """suara klik ketika puzzle berhasil ditempatkan"""
    click_sound.play()
    click_sound.set_volume(1.0)

def play_win_sound():
    """suara ketika puzzle selesai"""
    win_sound.set_volume(0.5)
    win_sound.play()

if __name__ == "__main__":
    print("Testing suara klik")
    play_click_sound()
    pygame.time.wait(1500)  # jeda 1,5 detik

    print("Testing suara menang")
    play_win_sound()
    pygame.time.wait(2000)  # jeda 2 detik