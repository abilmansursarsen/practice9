import pygame
from clock import MickeyClock


def main():
    pygame.init()

    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mickey's Clock")

    clock = pygame.time.Clock()
    mickey_clock = MickeyClock(width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mickey_clock.draw(screen)
        pygame.display.flip()

        # limit FPS
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()