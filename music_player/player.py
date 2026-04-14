import pygame
import os


class MusicPlayer:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        self.tracks = [
            os.path.join(base_dir, "music", "sample_tracks", "track1.mp3"),
            os.path.join(base_dir, "music", "sample_tracks", "track2.mp3")
        ]

        self.current_index = 0
        self.is_playing = False
        self.font = pygame.font.SysFont("Arial", 32)

    def load_current_track(self):
        track_path = self.tracks[self.current_index]

        if not os.path.exists(track_path):
            raise FileNotFoundError(f"Music file not found: {track_path}")

        pygame.mixer.music.load(track_path)

    def play(self):
        self.load_current_track()
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.tracks)
        self.play()

    def previous_track(self):
        self.current_index = (self.current_index - 1) % len(self.tracks)
        self.play()

    def get_current_track_name(self):
        return os.path.basename(self.tracks[self.current_index])

    def draw(self, screen):
        screen.fill((240, 240, 240))

        title = self.font.render("Music Player", True, (0, 0, 0))
        track = self.font.render(f"Track: {self.get_current_track_name()}", True, (0, 0, 0))
        status = self.font.render(
            f"Status: {'Playing' if self.is_playing else 'Stopped'}", True, (0, 0, 0)
        )

        controls_font = pygame.font.SysFont("Arial", 24)
        controls = [
            "P = Play",
            "S = Stop",
            "N = Next",
            "B = Previous",
            "Q = Quit"
        ]

        screen.blit(title, (50, 50))
        screen.blit(track, (50, 120))
        screen.blit(status, (50, 190))

        y = 280
        for control in controls:
            text = controls_font.render(control, True, (40, 40, 40))
            screen.blit(text, (50, y))
            y += 40