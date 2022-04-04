from weapon import Weapon
class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.sword = Weapon('Excalibur', 25)
        self.dagger = Weapon('Khopesh', 15)
        self.axe = Weapon('Leviathan', 30)
        self.weapon = Robot.weapon_choice(self)




    def attack(self, dinosaur):
        print(f'{self.name} attacks {dinosaur} with {self.weapon.name} for {self.weapon.attack_power} damage!')
        return self.weapon.attack_power

    def take_damage(self, damage):
        self.health -= damage
    
    def weapon_choice(self):
        choice = int(input('Choose your robots weapon:\n1 is the legendary Khopesh dagger.\n2 is the mythical Excalibur.\n3 is the great Leviathan axe.\nEnter your choice of 1, 2, or 3. '))
        if choice == 1:
            return self.dagger
        elif choice == 2:
            return self.sword
        elif choice == 3:
            return self.axe
        