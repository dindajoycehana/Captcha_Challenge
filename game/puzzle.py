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
        self.puzzle_size = 600
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
    
    def crop_center(self, frame, target_size):
        """Crop frame from center and resize to target size"""
        h, w = frame.shape[:2]
        
        # Get square crop from center
        size = min(h, w)
        start_y = (h - size) // 2
        start_x = (w - size) // 2
        
        cropped = frame[start_y:start_y+size, start_x:start_x+size]
        
        # Resize to target size
        resized = cv2.resize(cropped, (target_size, target_size))
        
        return resized
    
    def handle_hand_interaction(self, hand_landmarks, display):
        """Handle hand gesture interactions"""
        # Get hand position
        hand_pos = self.hand_tracker.get_hand_position(hand_landmarks, display.shape)
        cv2.circle(display, hand_pos, 8, (255, 0, 255), -1)
        
        # Check pinch gesture
        is_pinching = self.hand_tracker.is_pinching(hand_landmarks)
        
        if is_pinching:
            if self.selected_piece is None:
                # Select piece
                piece = self.puzzle_pieces.get_piece_at_position(
                    hand_pos, self.piece_size, self.puzzle_size
                )
                if piece:
                    self.selected_piece = piece
                    cv2.putText(display, "GRABBED!", (hand_pos[0] + 20, hand_pos[1]), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            if self.selected_piece is not None:
                # Release and swap
                target_piece = self.puzzle_pieces.get_piece_at_position(
                    hand_pos, self.piece_size, self.puzzle_size
                )
                if target_piece and target_piece['id'] != self.selected_piece['id']:
                    self.puzzle_pieces.swap_pieces(self.selected_piece, target_piece)
                    self.move_count += 1
                    play_click_sound() #play sound swap
                    self.solved = self.puzzle_pieces.check_solved()

                    if self.puzzle_pieces.check_solved():
                        self.solved = True
                        play_win_sound() #play win sound
                
                self.selected_piece = None
        
        # Show pinch status
        pinch_status = "PINCH" if is_pinching else "OPEN"
        color = (0, 255, 0) if is_pinching else (255, 255, 255)
        cv2.putText(display, pinch_status, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        return display
    
    def run(self):
        """Main game loop"""
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.flip(frame, 1)
            
            # Crop and resize frame to puzzle size
            cropped_frame = self.crop_center(frame, self.puzzle_size)
            frame_rgb = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2RGB)
            
            # Process hand detection only if game started AND not solved
            if self.game_started and not self.solved:
                results = self.hand_tracker.process_frame(frame_rgb)
            else:
                results = None
            
            # Create display frame
            if self.game_started:
                display = self.renderer.draw_puzzle(
                    cropped_frame, 
                    self.puzzle_pieces.pieces,
                    self.selected_piece,
                    self.solved
                )
            else:
                display = self.renderer.draw_start_screen(cropped_frame)
            
            # Handle hand tracking (only if game started AND not solved)
            if self.game_started and not self.solved and results and results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                
                # Draw hand landmarks
                self.hand_tracker.draw_landmarks(display, hand_landmarks)
                
                # Handle interactions
                display = self.handle_hand_interaction(hand_landmarks, display)
            
            # Show move count
            if self.game_started:
                display = self.renderer.draw_move_count(display, self.move_count)
            
            # Show solved screen
            if self.solved:
                display = self.renderer.draw_solved_screen(display, self.move_count)
            
            cv2.imshow('Live Glass Puzzle', display)
            
            # Handle keyboard input
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord(' ') and not self.game_started:
                # Start game and scramble glass blocks
                self.game_started = True
                self.puzzle_pieces.scramble()
            elif key == ord('r'):
                # Reset puzzle
                self.game_started = False
                self.solved = False
                self.move_count = 0
                self.selected_piece = None
                self.puzzle_pieces.scramble()
        
        cap.release()
        cv2.destroyAllWindows()
        self.hand_tracker.close()