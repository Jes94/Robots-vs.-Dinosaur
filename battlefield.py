from robot import Robot
from dinosaur import Dinosaur
from random import randint
class Battlefield:
    def __init__(self):
        self.game_name = "Robots versus Dinosaurs"
        pass

    def run_game(self):
        Battlefield.display_welcome(self)
        self.dino = Dinosaur(input('Please enter the name for the dinosaur. '), randint(15, 35))
        self.robot = Robot(input('Please enter the name for the robot fighter. '))
        Battlefield.battle_phase(self)
        Battlefield.display_winner(self)

    def display_welcome(self):
        print(f"Welcome to {self.game_name}")

    def battle_phase(self):
        while self.dino.health > 0 and self.robot.health > 0:
            self.dino.take_damage(self.robot.attack(self.dino.name))
            self.robot.take_damage(self.dino.attack(self.robot.name))
    def display_winner(self):
        if self.dino.health > self.robot.health:
            print(f'{self.dino.name} has defeated the mighty {self.robot.name}!')
        elif self.robot.health > self.dino.health:
            print(f'{self.robot.name} has slain the mighty {self.dino.name}!')
        elif self.dino.health <= 0 and self.robot.health <= 0:
            print("It's a double knockout!")
