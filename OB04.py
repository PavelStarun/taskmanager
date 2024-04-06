from abc import ABC, abstractmethod


class Fighter():
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def fight(self, monster):
        result = self.weapon.attack(monster)
        result.showOutcome()


class Monster():
    def __init__(self, name):
        self.name = name

    def die(self):
        print("Монстр побежден!")


class Weapon(ABC):
    @abstractmethod
    def attack(self, monster):
        pass


class Sword(Weapon):
    def attack(self, monster):
        print("Боец выбирает меч.")
        print("Боец наносит удар мечом.")
        return FighterWins()


class Bow(Weapon):
    def attack(self, monster):
        print("Боец выбирает лук.")
        print("Боец наносит удар из лука.")
        return FighterWins()


class Spear(Weapon):
    def attack(self, monster):
        print("Боец выбирает копье.")
        print("Боец наносит удар")
        print("Копье ломается")
        return MonsterWins()


class CombatResult(ABC):
    @abstractmethod
    def showOutcome(self):
        pass


class FighterWins(CombatResult):
    def showOutcome(self):
        print("Монстр побежден!")


class MonsterWins(CombatResult):
    def showOutcome(self):
        print("Монстр одержал победу над бойцом!")


monster = Monster("Монстр")
warrior = Fighter("Боец")
warrior.changeWeapon(Sword())
warrior.fight(monster)
warrior.changeWeapon(Bow())
warrior.fight(monster)
warrior.changeWeapon(Spear())
warrior.fight(monster)





