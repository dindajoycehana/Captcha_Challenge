"""
Game Renderer Module
Handles all visual rendering for the game
"""

import cv2
import numpy as np

class GameRenderer:
    def __init__(self, puzzle_size, piece_size):
        """Initialize renderer with puzzle dimensions"""
        self.puzzle_size = puzzle_size
        self.piece_size = piece_size
    
    def draw_puzzle(self, cropped_frame, pieces, selected_piece, solved):
        """Draw the glass puzzle showing live webcam through scrambled blocks"""
        display = np.zeros((self.puzzle_size, self.puzzle_size, 3), dtype=np.uint8)
        
        for piece in pieces:
            # Get the correct position (where this glass block looks at on webcam)
            correct_x, correct_y = piece['correct_pos']
            src_x = correct_x * self.piece_size
            src_y = correct_y * self.piece_size
            
            # Extract the view from the live webcam at correct position
            piece_view = cropped_frame[
                src_y:src_y+self.piece_size, 
                src_x:src_x+self.piece_size
            ].copy()
            
            # Get current position (where we draw this glass block)
            cx, cy = piece['current_pos']
            x = cx * self.piece_size
            y = cy * self.piece_size
            
            # Draw the glass block showing the webcam view
            display[y:y+self.piece_size, x:x+self.piece_size] = piece_view
            
            # Draw border around glass block
            if piece['current_pos'] == piece['correct_pos']:
                color = (0, 255, 0)  # Green for correct position
            else:
                color = (255, 255, 255)  # White for incorrect
            
            cv2.rectangle(
                display, 
                (x, y), 
                (x+self.piece_size, y+self.piece_size), 
                color, 
                2
            )
            
            # Highlight selected piece (only if not solved)
            if not solved and selected_piece and selected_piece['id'] == piece['id']:
                cv2.rectangle(
                    display, 
                    (x, y), 
                    (x+self.piece_size, y+self.piece_size), 
                    (0, 0, 255),  # Red for selected
                    4
                )
        
        return display
    
    def draw_start_screen(self, cropped_frame):
        """Draw the start screen with instructions"""
        display = cropped_frame.copy()
        overlay = display.copy()
        
        # Semi-transparent overlay
        cv2.rectangle(overlay, (0, 0), (self.puzzle_size, self.puzzle_size), (0, 0, 0), -1)
        display = cv2.addWeighted(display, 0.5, overlay, 0.5, 0)
        
        # Instructions text
        cv2.putText(
            display, 
            "Press SPACE", 
            (self.puzzle_size//2 - 120, self.puzzle_size//2 - 20), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            (0, 255, 255), 
            2
        )
        cv2.putText(
            display, 
            "to start puzzle", 
            (self.puzzle_size//2 - 130, self.puzzle_size//2 + 20), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            (0, 255, 255), 
            2
        )
        
        return display
    
    def draw_move_count(self, display, move_count):
        """Draw move counter"""
        cv2.putText(
            display, 
            f"Moves: {move_count}", 
            (10, self.puzzle_size - 10), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.7, 
            (255, 255, 255), 
            2
        )
        return display
    
    def draw_solved_screen(self, display, move_count):
        """Draw solved screen overlay"""
        overlay = display.copy()
        cv2.rectangle(
            overlay, 
            (0, 0), 
            (self.puzzle_size, self.puzzle_size), 
            (0, 255, 0), 
            -1
        )
        display = cv2.addWeighted(display, 0.7, overlay, 0.3, 0)
        
        # Solved text
        cv2.putText(
            display, 
            "SOLVED!", 
            (self.puzzle_size//2 - 100, self.puzzle_size//2 - 20), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1.5, 
            (255, 255, 255), 
            3
        )
        cv2.putText(
            display, 
            f"Moves: {move_count}", 
            (self.puzzle_size//2 - 80, self.puzzle_size//2 + 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            (255, 255, 255), 
            2
        )
        cv2.putText(
            display, 
            "Press 'R' to play again", 
            (self.puzzle_size//2 - 150, self.puzzle_size//2 + 70), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            0.7, 
            (255, 255, 255), 
            2
        )
        
        return display