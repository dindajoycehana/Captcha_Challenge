import cv2
import numpy as np

from .hand_tracker import HandTracker
from .puzzle_pieces import PuzzlePieces
from .game_renderer import GameRenderer
from .sound import play_click_sound, play_win_sound

class LiveGlassPuzzle:
    def __init__(self, grid_size=3):
        self.grid_size = grid_size
        self.total_pieces = grid_size * grid_size
        
        # Puzzle configuration (window size)
        self.puzzle_size = 500
        self.piece_size = self.puzzle_size // grid_size
        
        # Initialize components
        self.puzzle_pieces = PuzzlePieces(grid_size)
        self.hand_tracker = HandTracker()
        self.renderer = GameRenderer(self.puzzle_size, self.piece_size)
        
        # Hand tracking state
        self.selected_piece = None
        
        # Game state
        self.solved = False
        self.move_count = 0
        self.game_started = False
        self.selecting_grid = True  # NEW: state for grid selection

        # Mouse click storage
        self.last_click = None

    # ---------------------------------------------
    # Mouse callback for button clicking
    # ---------------------------------------------
    def mouse_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.last_click = (x, y)

    def crop_center(self, frame, target_size):
        h, w = frame.shape[:2]
        size = min(h, w)
        start_y = (h - size) // 2
        start_x = (w - size) // 2
        cropped = frame[start_y:start_y + size, start_x:start_x + size]
        return cv2.resize(cropped, (target_size, target_size))
    
    def reinitialize_game(self, new_grid_size):
        """Reinitialize game components with new grid size"""
        self.grid_size = new_grid_size
        self.total_pieces = new_grid_size * new_grid_size
        self.piece_size = self.puzzle_size // new_grid_size
        
        # Reinitialize components
        self.puzzle_pieces = PuzzlePieces(new_grid_size)
        self.renderer = GameRenderer(self.puzzle_size, self.piece_size)
        
        # Reset game state
        self.selected_piece = None
        self.solved = False
        self.move_count = 0
    
    def handle_hand_interaction(self, hand_landmarks, display):
        hand_pos = self.hand_tracker.get_hand_position(hand_landmarks, display.shape)
        cv2.circle(display, hand_pos, 8, (255, 0, 255), -1)
        
        is_pinching = self.hand_tracker.is_pinching(hand_landmarks)
        
        if is_pinching:
            if self.selected_piece is None:
                piece = self.puzzle_pieces.get_piece_at_position(
                    hand_pos, self.piece_size, self.puzzle_size
                )
                if piece:
                    self.selected_piece = piece
                    cv2.putText(display, "GRABBED!", (hand_pos[0] + 20, hand_pos[1]), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            if self.selected_piece is not None:
                target_piece = self.puzzle_pieces.get_piece_at_position(
                    hand_pos, self.piece_size, self.puzzle_size
                )
                if target_piece and target_piece['id'] != self.selected_piece['id']:
                    self.puzzle_pieces.swap_pieces(self.selected_piece, target_piece)
                    self.move_count += 1
                    play_click_sound()
                    self.solved = self.puzzle_pieces.check_solved()

                    if self.solved:
                        play_win_sound()
                
                self.selected_piece = None

        pinch_status = "PINCH" if is_pinching else "OPEN"
        color = (0, 255, 0) if is_pinching else (255, 255, 255)

        # Hitung ukuran teks untuk rata kanan otomatis
        (text_w, text_h), _ = cv2.getTextSize(
            pinch_status, cv2.FONT_HERSHEY_SIMPLEX, 0.65, 2
        )

        x = self.renderer.puzzle_size - text_w - 20   
        y = self.renderer.header_h + 25                  

        cv2.putText(display, pinch_status,
                    (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65,
                    color, 2)

        return display

    # ===============
    # MAIN GAME LOOP
    # ===============
    def run(self):
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        # Register window + mouse callback (IMPORTANT)
        cv2.namedWindow("Live Glass Puzzle")
        cv2.setMouseCallback("Live Glass Puzzle", self.mouse_event)
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.flip(frame, 1)
            cropped_frame = self.crop_center(frame, self.puzzle_size)
            frame_rgb = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB)
            
            # HAND TRACKING
            if self.game_started and not self.solved:
                results = self.hand_tracker.process_frame(frame_rgb)
            else:
                results = None
            
            # DISPLAY
            if self.selecting_grid:
                # Show grid selection menu
                display = self.renderer.draw_grid_selection_menu(cropped_frame)
                
            elif self.game_started:
                display = self.renderer.draw_puzzle(
                    cropped_frame, 
                    self.puzzle_pieces.pieces,
                    self.selected_piece,
                    self.solved
                )

                # Header + Footer
                display = self.renderer.draw_recaptcha_header(
                    display,
                    title="CAPTCHA Challenge",
                    subtitle=f"Solve the {self.grid_size}x{self.grid_size} puzzle"
                )
                display = self.renderer.draw_recaptcha_footer(display, solved=self.solved)

            else:
                display = cropped_frame.copy()
                display = self.renderer.draw_recaptcha_header(
                    display,
                    title="CAPTCHA Challenge",
                    subtitle="Press SPACE to start or Q to quit"
                )
            
            # HAND GESTURE
            if self.game_started and not self.solved and results and results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                self.hand_tracker.draw_landmarks(display, hand_landmarks)
                display = self.handle_hand_interaction(hand_landmarks, display)
            
            # MOVE COUNT
            if self.game_started:
                display = self.renderer.draw_move_count(display, self.move_count)

            # SOLVED SCREEN
            if self.solved:
                display = self.renderer.draw_solved_screen(display, self.move_count)

            # ----------------------------------------------------
            # HANDLE MOUSE CLICKS
            # ----------------------------------------------------
            if self.last_click:
                mx, my = self.last_click
                self.last_click = None  # reset click

                # GRID SELECTION
                if self.selecting_grid:
                    selected_grid = self.renderer.check_grid_button_click(mx, my)
                    if selected_grid:
                        print(f"Selected grid: {selected_grid}x{selected_grid}")
                        self.reinitialize_game(selected_grid)
                        self.selecting_grid = False
                        self.game_started = True
                        self.puzzle_pieces.scramble()

                # GAME BUTTONS
                elif self.game_started:
                    footer_y = self.renderer.header_h + self.puzzle_size

                    # QUIT BUTTON
                    if 20 <= mx <= 150 and footer_y + 10 <= my <= footer_y + 55:
                        print("QUIT CLICKED")
                        break

                    # PLAY AGAIN / VERIFY BUTTON
                    btn_x1 = self.puzzle_size - 210
                    btn_x2 = self.puzzle_size - 20

                    if btn_x1 <= mx <= btn_x2 and footer_y + 10 <= my <= footer_y + 55:
                        print("PLAY AGAIN CLICKED")
                        self.selecting_grid = True
                        self.game_started = False
                        self.solved = False
                        self.move_count = 0
                        self.selected_piece = None

            # SHOW DISPLAY
            cv2.imshow("Live Glass Puzzle", display)
            
            # KEYBOARD INPUT
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord(' '):
                if self.selecting_grid:
                    # Space bar doesn't work during grid selection
                    pass
                elif not self.game_started:
                    self.game_started = True
                    self.puzzle_pieces.scramble()
        
        cap.release()
        cv2.destroyAllWindows()
        self.hand_tracker.close()