from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

class PowerUp(Sprite):
    def __init__(self, image, type):
        print("power")
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.y = 125
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, powerups):
        self.rect.x -= game_speed
        if self.rect.x < 0:
            powerups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)