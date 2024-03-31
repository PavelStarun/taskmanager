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
        return self.items.get(product, "Продукт не найден")

    def update_price(self, product, new_price):
        if product in self.items:
            self.items[product] = new_price
        else:
            "Продукт не найдет для обновления цены"

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
    action = input("Выберите действие: 'добавить', 'удалить', 'узнать', 'поменять' или введите 'стоп' для выхода: ").lower()
    if action == 'стоп':
        break
        
    if action == 'добавить':
        print("Список магазинов")
        for shop_key in shops:
            print(f"{shop_key}: {shops[shop_key].name}, {shops[shop_key].address}")
        print("6: Во все магазины")

        number_shop = input("Введите № магазина или 'стоп' чтобы закончить: ")
        if number_shop.lower() == 'стоп':
            break

        if number_shop in shops or number_shop == '6':
            product = input("Введите название продукта для добавления его в магазин: ")
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

    elif action == 'удалить':
        print("Список магазинов")
        for shop_key in shops:
            print(f"{shop_key}: {shops[shop_key].name}, {shops[shop_key].address}")
        print("6: товар удален из всех магазинов")
        remove_product = input("Введите № магазина или 'стоп' чтобы закончить: ")
        if remove_product == 'стоп':
            break
        if remove_product in shops or remove_product == '6':
            product_del = input("Введите название продукта для удаления: ")

            if remove_product == '6':
                for shop in shops.values():
                    shop.remove_product(product)
                print("Товар удален со всех магазинов.")
            else:
                shops[number_shop].remove_product(product, price)
                print(f"Товар удален из {shops[number_shop].name}, по адресу {shops[number_shop].address}.")
        else:
            print("Неверный выбор, попробуйте снова.")



    elif action == 'узнать':
        product_name = input("Введите название продукта, чтобы узнать цену: ")
        print("Список магазинов:")
        for shop_key in shops:
            print(f"{shop_key}: {shops[shop_key].name}, {shops[shop_key].address}")
        print("6: Во всех магазинах")

        number_shop = input("Введите № магазина или 'стоп' чтобы закончить: ").lower()
        if number_shop == 'стоп':
            break

        elif number_shop == '6':
            for shop_key, shop in shops.items():
                price = shop.get_price(product_name)
                if price is not None:
                    print(f"В магазине '{shop.name}', по адресу '{shop.address}', цена продукта '{product_name}': {price}")
                else:
                    print(f"В магазине '{shop.name}', по адресу '{shop.address}', продукт '{product_name}' не найден.")

        elif number_shop in shops:
            price = shops[number_shop].get_price(product_name)
            if price is not None:
                print(f"В магазине '{shops[number_shop].name}', по адресу '{shops[number_shop].address}', цена продукта '{product_name}': {price}")
            else:
                print(f"Продукт '{product_name}' не найден в магазине {shops[number_shop].name}.")

        else:
            print("Неверный выбор, попробуйте снова.")



    elif action == 'поменять':
        product_name = input("Введите название продукта, чью цену нужно обновить: ")
        new_price_input = input("Введите новую цену продукта: ")

        try:
            new_price = float(new_price_input)
        except ValueError:
            print("Введена некорректная цена. Пожалуйста, используйте числовой формат.")
            continue

        print("Список магазинов:")
        for shop_key in shops:
            print(f"{shop_key}: {shops[shop_key].name}, {shops[shop_key].address}")
        print("6: Во всех магазинах")
        number_shop = input("Введите № магазина, в котором нужно обновить цену, или 'стоп' для отмены: ").lower()
        if number_shop == 'стоп':
            break

        elif number_shop in shops:
            if product_name in shops[number_shop].items:
                shops[number_shop].update_price(product_name, new_price)
                print(f"Цена продукта '{product_name}' обновлена в магазине {shops[number_shop].name}.")

            else:
                print(f"Продукт '{product_name}' не найден в магазине {shops[number_shop].name}.")

        elif number_shop == '6':
            for shop_key, shop in shops.items():
                if product_name in shop.items:
                    shop.update_price(product_name, new_price)
                    print(f"Цена продукта '{product_name}' обновлена в магазине {shop.name}.")

            else:
                print(f"Продукт '{product_name}' не найден в магазине {shop.name}.")

    else:
        print("Неверный выбор, попробуйте снова.")

print("Список всех магазинов и товаров:")
for key, shop in shops.items():
    print(f"{key} ({shop.name}, {shop.address}): {shop.list_products() if shop.items else 'Нет товаров'}")
