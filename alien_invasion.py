import sys
import pygame
from settings import Settings
from rocket import Rocket

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # General settings
        self.settings = Settings()
        # Screen
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption(self.settings.title)
        # Rocket
        self.rocket = Rocket(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Get events
            self.get_events()
            self.rocket.update()
            self.update_screen()

            
    
    def get_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move to the right.
                    self.rocket.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = False
    
    def update_screen(self):
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.color)
        self.rocket.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()