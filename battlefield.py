from robot import Robot
from dinosaur import Dinosaur
class Battlefield:
    def __init__(self):
        self.game_name = "Robots versus Dinosaurs"
        pass

    def run_game(self):
        self.display_welcome()
        self.dino = Dinosaur(input('Please enter the name for the dinosaur. '), int(input('Enter how stron the dinosaur should be. Pick a number 15-35: ')))
        self.robot = Robot(input('Please enter the name for the robot fighter. '))
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(f"Welcome to {self.game_name}")

    def battle_phase(self):
        counter = 0
        while counter == 0:
            if self.robot.health > 0:
                self.dino.take_damage(self.robot.attack(self.dino.name))
            else:
                counter += 1
            if self.dino.health > 0:
                self.robot.take_damage(self.dino.attack(self.robot.name))
            else:
                counter += 1
    def display_winner(self):
        if self.dino.health > self.robot.health:
            print(f'{self.dino.name} has defeated the mighty {self.robot.name}!')
        elif self.robot.health > self.dino.health:
            print(f'{self.robot.name} has slain the mighty {self.dino.name}!')
