import random

class PuzzlePieces:
    def __init__(self, grid_size):
        """Initialize puzzle pieces"""
        self.grid_size = grid_size
        self.pieces = []
        self.create_pieces()
        
    def create_pieces(self):
        """Create puzzle pieces with correct and current positions"""
        self.pieces = []
        
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.pieces.append({
                    'correct_pos': (col, row),
                    'current_pos': (col, row),
                    'id': row * self.grid_size + col
                })
    
    def scramble(self):
        """Scramble the puzzle pieces"""
        positions = [
            (col, row) 
            for row in range(self.grid_size) 
            for col in range(self.grid_size)
        ]
        random.shuffle(positions)
        
        for i, piece in enumerate(self.pieces):
            piece['current_pos'] = positions[i]
    
    def get_piece_at_position(self, pos, piece_size, puzzle_size):
        """Get puzzle piece at screen position"""
        x, y = pos
        
        # Check if position is within puzzle area
        if x < 0 or x >= puzzle_size or y < 0 or y >= puzzle_size:
            return None
        
        # Calculate grid position
        grid_x = x // piece_size
        grid_y = y // piece_size
        
        # Find piece at this grid position
        for piece in self.pieces:
            if piece['current_pos'] == (grid_x, grid_y):
                return piece
        
        return None
    
    def swap_pieces(self, piece1, piece2):
        """Swap positions of two puzzle pieces"""
        piece1['current_pos'], piece2['current_pos'] = \
            piece2['current_pos'], piece1['current_pos']
    
    def check_solved(self):
        """Check if puzzle is solved"""
        for piece in self.pieces:
            if piece['current_pos'] != piece['correct_pos']:
                return False
        return True