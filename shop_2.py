class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_product(self, product, price):
        self.items[product] = price
        print(f"Товар {product} был добавлен в {self.name} по адресу {self.address} по цене {price}")

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]
            print(f"Товар {product} был удален из {self.name} по адресу {self.address}")

    def get_price(self, product):
        return self.items.get(product)

    def update_price(self, product, new_price):
        if product in self.items:
            self.items[product] = new_price
            print(f"Цена на товар {product} обновлена в {self.name} по адресу {self.address} на новую цену {new_price}")
        else:
            print(f"Продукт {product} не найдет для обновления цены")


shop1 = Store("evroopt", "Минск, Руссиянова 6")
shop2 = Store("evroopt", "Минск, Независимости 195")
shop3 = Store("evroopt", "Минск, Толстого 10")
shop4 = Store("evroopt", "Минск, Дзержинского 17")
shop5 = Store("evroopt", "Брест, Гоголя 84")


shop1.add_product("банан", 3.73)
shop2.add_product("клубника", 5.66)
shop3.add_product("колбаса", 12.54)

shop1.remove_product("банан")

print(shop2.get_price("клубника"))

shop3.update_price("колбаса", 12.99)