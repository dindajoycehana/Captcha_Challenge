from game.puzzle import LiveGlassPuzzle

def main():
    """Main entry point for the game"""
    try:
        print("🪟 CAPTCHA CHALLENGE")
        print("=" * 50)
        print("Instructions:")
        print("1. Select difficulty level (3x3, 4x4, or 5x5)")
        print("2. Pinch (thumb + index) to grab a glass block")
        print("3. Move hand to another block while pinching")
        print("4. Release pinch to swap blocks")
        print("5. Arrange blocks so each views the correct part of webcam")
        print("6. Press 'Q' to quit")
        print("=" * 50)
        
        # Create and run the puzzle game (starts with menu)
        puzzle = LiveGlassPuzzle()  
        puzzle.run()
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure to:")
        print("1. Install required packages: pip install opencv-python mediapipe numpy")
        print("2. Have a webcam connected")
        print("3. Grant webcam permissions to the application")

if __name__ == "__main__":
    main()