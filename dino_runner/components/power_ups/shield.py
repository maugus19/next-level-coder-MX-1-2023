from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SHIELD_TYPE, SHIELD

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)
