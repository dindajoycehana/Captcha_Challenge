# Hand Tracking using mediapipe

import mediapipe as mp
import math

class HandTracker:
    def __init__(self):
        """Initialize MediaPipe hand tracking"""
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # Pinch detection threshold (Jarak antara ibu jari dan jari telunjuk)
        self.pinch_threshold = 0.05
    
    def process_frame(self, frame_rgb):
        """Process frame for hand detection"""
        return self.hands.process(frame_rgb)
    
    def get_hand_position(self, hand_landmarks, frame_shape):
        """Get normalized hand position from index finger tip"""
        h, w = frame_shape[:2]
        index_tip = hand_landmarks.landmark[8]
        return (int(index_tip.x * w), int(index_tip.y * h))
    
    def is_pinching(self, hand_landmarks):
        """Detect pinch gesture (thumb tip close to index finger tip)"""
        thumb_tip = hand_landmarks.landmark[4]
        index_tip = hand_landmarks.landmark[8]
        
        distance = math.sqrt(
            (thumb_tip.x - index_tip.x)**2 + 
            (thumb_tip.y - index_tip.y)**2
        )
        
        return distance < self.pinch_threshold
    
    def draw_landmarks(self, frame, hand_landmarks):
        """Draw hand landmarks on frame"""
        self.mp_draw.draw_landmarks(
            frame, 
            hand_landmarks, 
            self.mp_hands.HAND_CONNECTIONS
        )
    
    def close(self):
        """Clean up resources"""
        self.hands.close()