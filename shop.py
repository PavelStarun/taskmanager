class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_product(self, product, price):
        self.items[product] = price

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]

    def get_price(self, product):
        return self.items.get(product, None)

    def update_price(self, product, new_price):
        if product in self.items:
            self.items[product] = new_price


    def list_products(self):
        return ", ".join([f"{product}: {price}" for product, price in self.items.items()])


# Создание магазинов
shops = {
    "1": Store("evroopt", "Минск, Руссиянова 6"),
    "2": Store("evroopt", "Минск, Независимости 195"),
    "3": Store("evroopt", "Минск, Толстого 10"),
    "4": Store("evroopt", "Минск, Дзержинского 17"),
    "5": Store("evroopt", "Брест, Гогаля 84")
}

while True:
    action = input("Выберите действия и пропишите его: добавить, удалить 'товар'; или узнать, поменять 'цену' на товар - ")
    if action == 'стоп':
        break
        
    if action.lower() == 'добавить':
        print("Список магазинов")
        for shop_key in shops:
            print(f"{shop_key}: {shops[shop_key].name}, {shops[shop_key].address}")
        print("6: Во все магазины")

        number_shop = input("Введите № магазина или 'стоп' чтобы закончить: ")
        if number_shop.lower() == 'стоп':
            break

        if number_shop in shops or number_shop == '6':
            product = input("Введите название продукта: ")
            price = input("Введите цену продукта: ")

            if number_shop == '6':
                for shop in shops.values():
                    shop.add_product(product, price)
                print("Товар добавлен во все магазины.")
            else:
                shops[number_shop].add_product(product, price)
                print(f"Товар добавлен в {shops[number_shop].name}, по адресу {shops[number_shop].address}.")
        else:
            print("Неверный выбор, попробуйте снова.")

    elif action.lower() == 'удалить':
        print("Список магазинов")
        for shop_key in shops:
            print(f"{shop_key}: {shops[shop_key].name}, {shops[shop_key].address}")
        print("6: Из всех магазинов")
        del_produkt = input("Введите № магазина или 'стоп' чтобы закончить: ")
        if del_produkt.lower() == 'стоп':
            break
        if del_produkt in shops or del_produkt == '6':
            product = input("Введите название продукта для удаления: ")

            if del_produkt == '6':
                for shop in shops.values():
                    shop.del_product(product)
                print("Товар удален со всех магазинов.")
            else:
                shops[number_shop].add_product(product, price)
                print(f"Товар удален из {shops[number_shop].name}, по адресу {shops[number_shop].address}.")
        else:
            print("Неверный выбор, попробуйте снова.")

    if action == 'узнать':









print("Список всех магазинов и товаров:")
for key, shop in shops.items():
    print(f"{key} ({shop.name}, {shop.address}): {shop.list_products() if shop.items else 'Нет товаров'}")
