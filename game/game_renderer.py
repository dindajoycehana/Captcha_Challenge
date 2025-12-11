import cv2
import numpy as np


class GameRenderer:
    def __init__(self, puzzle_size, piece_size):
        self.puzzle_size = puzzle_size
        self.piece_size = piece_size

        # FIXED: header & footer lebih kecil dan proporsional
        self.header_h = 65
        self.footer_h = 60

        self.total_height = self.header_h + puzzle_size + self.footer_h


    # ============================================================
    # DRAW GRID SELECTION MENU
    # ============================================================
    def draw_grid_selection_menu(self, cropped_frame):
        """Draw the initial grid selection menu with 3x3, 4x4, 5x5 options"""
        display = cropped_frame.copy()
        
        # Draw header
        display = self.draw_recaptcha_header(
            display,
            title="CAPTCHA Challenge",
            subtitle="Select puzzle difficulty to start"
        )
        
        # Menu area (center of puzzle area)
        menu_y_start = self.header_h + 100
        button_width = 140
        button_height = 120
        spacing = 20
        
        # Calculate total width to center buttons
        total_width = (button_width * 3) + (spacing * 2)
        start_x = (self.puzzle_size - total_width) // 2
        
        # Grid options with colors
        grid_options = [
            {"size": 3, "label": "3x3", "difficulty": "EASY", "color": (76, 175, 80)},
            {"size": 4, "label": "4x4", "difficulty": "MEDIUM", "color": (33, 150, 243)},
            {"size": 5, "label": "5x5", "difficulty": "HARD", "color": (103, 58, 183)}
        ]
        
        for i, option in enumerate(grid_options):
            x = start_x + (i * (button_width + spacing))
            y = menu_y_start
            
            # Draw button background
            cv2.rectangle(display, (x, y), (x + button_width, y + button_height), 
                         option["color"], -1)
            
            # Draw button border
            cv2.rectangle(display, (x, y), (x + button_width, y + button_height), 
                         (255, 255, 255), 3)
            
            # Draw grid size label (large)
            label = option["label"]
            (text_w, text_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 1.8, 3)
            text_x = x + (button_width - text_w) // 2
            text_y = y + 55
            cv2.putText(display, label, (text_x, text_y),
                       cv2.FONT_HERSHEY_SIMPLEX, 1.8, (255, 255, 255), 3)
            
            # Draw difficulty label (small)
            difficulty = option["difficulty"]
            (text_w2, text_h2), _ = cv2.getTextSize(difficulty, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
            text_x2 = x + (button_width - text_w2) // 2
            text_y2 = y + 95
            cv2.putText(display, difficulty, (text_x2, text_y2),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # Store button positions for click detection
        self.grid_buttons = []
        for i, option in enumerate(grid_options):
            x = start_x + (i * (button_width + spacing))
            y = menu_y_start
            self.grid_buttons.append({
                "size": option["size"],
                "x1": x,
                "y1": y,
                "x2": x + button_width,
                "y2": y + button_height
            })
        
        return display


    def check_grid_button_click(self, x, y):
        """Check if a grid button was clicked and return the grid size"""
        if not hasattr(self, 'grid_buttons'):
            return None
        
        for button in self.grid_buttons:
            if button["x1"] <= x <= button["x2"] and button["y1"] <= y <= button["y2"]:
                return button["size"]
        return None


    # ============================================================
    # DRAW PUZZLE GRID
    # ============================================================
    def draw_puzzle(self, cropped_frame, pieces, selected_piece, solved):
        display = np.zeros((self.total_height, self.puzzle_size, 3), dtype=np.uint8)

        for piece in pieces:
            correct_x, correct_y = piece["correct_pos"]

            src_x = correct_x * self.piece_size
            src_y = correct_y * self.piece_size

            piece_view = cropped_frame[
                src_y:src_y + self.piece_size,
                src_x:src_x + self.piece_size
            ].copy()

            cx, cy = piece["current_pos"]
            x = cx * self.piece_size
            y = cy * self.piece_size + self.header_h

            display[y:y + self.piece_size, x:x + self.piece_size] = piece_view

            # highlight border
            color = (0, 255, 0) if piece["current_pos"] == piece["correct_pos"] else (255, 255, 255)
            cv2.rectangle(display, (x, y), (x + self.piece_size, y + self.piece_size), color, 2)

            if not solved and selected_piece and selected_piece["id"] == piece["id"]:
                cv2.rectangle(display, (x, y), (x + self.piece_size, y + self.piece_size), (0, 0, 255), 3)

        return display


    # ============================================================
    # HEADER
    # ============================================================
    def draw_recaptcha_header(self, display, title="reCAPTCHA Challenge", subtitle=""):
        cv2.rectangle(display, (0, 0), (self.puzzle_size, self.header_h), (255, 138, 0), -1)

        # FIXED: Lebih kecil & rapi
        cv2.putText(display, title, (18, 32),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.85, (255, 255, 255), 2)

        cv2.putText(display, subtitle, (18, 58),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

        return display


    # ============================================================
    # FOOTER
    # ============================================================
    def draw_recaptcha_footer(self, display, solved=False):
        y1 = self.header_h + self.puzzle_size

        # footer background
        cv2.rectangle(display, (0, y1),
                      (self.puzzle_size, y1 + self.footer_h),
                      (245, 245, 245), -1)

        cv2.rectangle(display, (0, y1),
                      (self.puzzle_size, y1 + self.footer_h),
                      (200, 200, 200), 2)

        # Quit
        cv2.rectangle(display, (20, y1 + 10), (150, y1 + 50), (230, 230, 230), -1)
        cv2.rectangle(display, (20, y1 + 10), (150, y1 + 50), (120, 120, 120), 2)

        cv2.putText(display, "QUIT", (55, y1 + 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

        # RESTART / PLAY AGAIN button
        bx1 = self.puzzle_size - 210
        bx2 = self.puzzle_size - 20

        cv2.rectangle(display, (bx1, y1 + 10), (bx2, y1 + 50), (0, 120, 255), -1)
        cv2.rectangle(display, (bx1, y1 + 10), (bx2, y1 + 50), (0, 70, 180), 2)

        label = "PLAY AGAIN" if solved else "RESTART"

        # --- auto center text ---
        (text_w, text_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.65, 2)
        btn_center_x = bx1 + (bx2 - bx1) // 2
        text_x = btn_center_x - text_w // 2
        text_y = y1 + 38

        cv2.putText(display, label,
                    (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)


        return display


    # ============================================================
    # MOVE COUNTER – dipindahkan KE BAWAH HEADER agar tidak tabrakan
    # ============================================================
    def draw_move_count(self, display, move_count):
        cv2.putText(display,
                    f"Moves: {move_count}",
                    (10, self.header_h + 25),      # FIXED: turun ke bawah header
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65,
                    (255, 255, 255), 2)
        return display


    # ============================================================
    # SOLVED OVERLAY
    # ============================================================
    def draw_solved_screen(self, display, move_count):
        overlay = display.copy()

        cv2.rectangle(overlay, (0, self.header_h),
                      (self.puzzle_size, self.header_h + self.puzzle_size),
                      (0, 255, 0), -1)

        display = cv2.addWeighted(display, 0.65, overlay, 0.35, 0)

        cx = self.puzzle_size // 2 - 130
        cy = self.header_h + self.puzzle_size // 2 - 20

        cv2.putText(display, "SOLVED!",
                    (cx, cy),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.6,
                    (255, 255, 255), 3)

        cv2.putText(display, f"Moves: {move_count}",
                    (cx + 35, cy + 55),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (255, 255, 255), 2)

        return display