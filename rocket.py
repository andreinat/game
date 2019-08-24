import pygame

class Rocket:
    """Rocket representation"""
    def __init__(self, ai_game):
        # set the initial position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        # load the image and get the rect
        self.image = pygame.image.load('img/rocket.bmp')
        self.rect = self.image.get_rect()
           
        # Set the position
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
    
    def update(self):
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

