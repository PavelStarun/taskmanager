import random


class Hero():
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} с {self.attack_power} уроном.")
        print(f"{other.name} осталось {other.health} здоровья.")
        print(f"| {self.name} | {self.health} | {other.name} | {other.health} |")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.player.name} победил!")
                break
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.computer.name} победил!")
                break

warrior = Hero("Игрок", 100, 20)
computer = Hero("Компьютер", random.randint(70, 100), random.randint(10, 40))
game = Game(warrior, computer)
game.start()
