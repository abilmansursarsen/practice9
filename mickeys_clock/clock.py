import pygame
import math
import datetime
import os


class MickeyClock:
    def __init__(self, width=800, height=800):
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)

        image_path = os.path.join("images", "mickeyclock.png")
        self.background = pygame.image.load(image_path)
        self.background = pygame.transform.scale(self.background, (width, height))

        # Hand lengths
        self.minute_hand_length = 170
        self.second_hand_length = 150

        # Colors
        self.minute_color = (0, 0, 0)       # black
        self.second_color = (255, 0, 0)     # red
        self.center_color = (30, 30, 30)

        # Font
        self.font = pygame.font.SysFont("Arial", 36, bold=True)

    def get_current_time(self):
        now = datetime.datetime.now()
        return now.minute, now.second

    def calculate_angle(self, value, max_value):
        """
        Pygame coordinates:
        - 0 degrees should point up
        - clockwise positive visually
        """
        return (360 * value / max_value) - 90

    def draw_hand(self, screen, angle_degrees, length, color, thickness):
        angle_radians = math.radians(angle_degrees)
        x = self.center[0] + math.cos(angle_radians) * length
        y = self.center[1] + math.sin(angle_radians) * length

        pygame.draw.line(screen, color, self.center, (x, y), thickness)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        minute, second = self.get_current_time()

        # Angles
        minute_angle = self.calculate_angle(minute, 60)
        second_angle = self.calculate_angle(second, 60)

        # Draw hands
        self.draw_hand(screen, minute_angle, self.minute_hand_length, self.minute_color, 8)
        self.draw_hand(screen, second_angle, self.second_hand_length, self.second_color, 5)

        # Draw center
        pygame.draw.circle(screen, self.center_color, self.center, 12)

        # Draw digital time
        time_text = self.font.render(f"{minute:02}:{second:02}", True, (0, 0, 0))
        text_rect = time_text.get_rect(center=(self.width // 2, self.height - 40))
        screen.blit(time_text, text_rect)