from abc import ABC, abstractmethod
import random


class Weapon(ABC):
    name = "Неизвестное оружие"

    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    name = "Меч"
    def attack(self):
        print("Боец выбирает меч.")
        return 55


class Bow(Weapon):
    name = "Лук"
    def attack(self):
        print("Боец выбирает лук.")
        return 42


class Spear(Weapon):
    name = "Копье"
    def attack(self):
        print("Боец выбирает копье.")
        return 30


class Fighter:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
        self.weapon = None
        self.weapons = [Sword(), Bow(), Spear()]

    def changeWeapon(self):
        self.weapon = random.choice(self.weapons)
        print(f"{self.name} меняет оружие.")

    def fight(self, monster):
        while self.hp > 0 and monster.hp > 0:
            self.changeWeapon()
            damage = self.weapon.attack()
            monster.hp -= damage
            print(f"{self.name} наносит урон {damage} с помощью {self.weapon.name}. Здоровье монстра: {monster.hp}")
            if monster.hp <= 0:
                print("Монстр побежден!")
                break

            monster.attack(self)
            if self.hp <= 0:
                print("Монстр одержал победу над бойцом!")


class Monster:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp

    def attack(self, fighter):
        damage = random.randint(30, 70)
        fighter.hp -= damage
        print(f"Монстр наносит урон {damage}. Здоровье {fighter.name}: {fighter.hp}")



monster = Monster("Монстр")
warrior = Fighter("Боец")
warrior.fight(monster)
