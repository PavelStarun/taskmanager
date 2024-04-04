class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Звуки животных")

    def eat(self):
        print("Еда животных")


class Bird(Animal):
    def eat(self):
        print("Птицы в основном питаются личинками и червяками")
    def make_sound(self):
        print("В языке птиц насчитываются десятки звуковых сигналов (бедствия, предостережения, пищевые, ухаживания, спаривания, агрессивные, стайные, гнездовые и т. д.)")

class Mammal(Animal):

    def eat(self):
        print("Млекопитающие в основном растительноядные и плотоядные")

    def make_sound(self):
        print("Могут издавать разные звуки")

class Reptile(Animal):
    def eat(self):
        print("Рептилии в основном плотоядные")

    def make_sound(self):
        print("Рептилии в основном издают звуки шипения или свист")



def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


def animal_eat(animals):
    for animal in animals:
        animal.eat()


class Zoo():
    def __init__(self):
        self.animals = []
        self.zookeepers = []
        self.veterinarians = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_zookeeper(self, zookeeper):
        self.zookeepers.append(zookeeper)

    def add_veterinarian(self, veterinarian):
        self.veterinarians.append(veterinarian)

    def list_animals(self):
        for animal in self.animals:
            print(animal)

    def list_zookeepers(self):
        for zookeeper in self.zookeepers:
            print(zookeeper)

    def list_veterinarians(self):
        for veterinarian in self.veterinarians:
            print(veterinarian)


    def info_zoo(self):
        info = "Животные в зоопарке:\n"
        for animal in self.animals:
            info += f" - {type(animal).__name__}: {animal.name}, {animal.age} лет\n"
        info += "\nСотрудники зоопарка:\n"
        for zookeeper in self.zookeepers:
            info += f" - {type(zookeeper).__name__}: {zookeeper.name}, {zookeeper.age} лет, {zookeeper.post}\n"
        for veterinarian in self.veterinarians:
            info += f" - {type(veterinarian).__name__}: {veterinarian.name}, {veterinarian.age} лет\n"
        return info

    def save_info_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.info_zoo())

    def load_info_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read())


class ZooKeeper(Zoo):
    def __init__(self, name, age, post):
        self.name = name
        self.age = age
        self.post = post

    def feed_animal(self, animal):
        print(f"{self.name} cмотрит {animal}")


class Veterinarian(Zoo):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal}")




zoo = Zoo()
zoo.add_animal(Bird("Павлин", 2))
zoo.add_animal(Mammal("Медведь", 5))
zoo.add_animal(Reptile("Змея", 3))
zoo.add_zookeeper(ZooKeeper("Артем", 45, "Менеджер"))
zoo.add_veterinarian(Veterinarian("Виктор", 35))
zoo.add_animal(Bird("Попугая 'Гоша'", 4))
zoo.add_animal(Mammal("Лев", 7))
zoo.add_animal(Reptile("Кролик 'Белый'", 2))
zoo.add_veterinarian(Veterinarian("Антон", 40))
zoo.add_zookeeper(ZooKeeper("Василий", 55, "Директор"))

print(zoo.info_zoo())

zoo.save_info_to_file('zoo_info.txt')

zoo.load_info_from_file('zoo_info.txt')

