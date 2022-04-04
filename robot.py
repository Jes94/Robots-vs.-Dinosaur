from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.sword = Weapon('Excalibur', 25)

    def attack(self, dinosaur):
        print(f'{self.name} attacks {dinosaur} with {self.sword.name} for {self.sword.attack_power} damage!')
        return self.sword.attack_power

    def take_damage(self, damage):
        self.health -= damage