class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_product(self, product, price):
        self.items[product] = price

    def del_product(self, product):
        if product in self.items:
            del self.items[product]

    def remove_product(self, product):
        if product in self.items:
            del self.items[product]

    def get_price(self, product):
        return self.items.get(product, None)

    def update_price(self, product, price):
        if product in self.items:
            self.items[product] = price


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
    print("Список магазинов")
    for shop_key in shops:
        print(f"{shop_key}: {shops[shop_key].name}, {shops[shop_key].address}")
    print("6: Во все магазины")

    magaz = input("Введите № магазина или 'стоп' чтобы закончить: ")
    if magaz.lower() == 'стоп':
        break

    if magaz in shops or magaz == '6':
        product = input("Введите название продукта: ")
        price = input("Введите цену продукта: ")

        if magaz == '6':
            for shop in shops.values():
                shop.add_product(product, price)
            print("Товар добавлен во все магазины.")
        else:
            shops[magaz].add_product(product, price)
            print(f"Товар добавлен в {shops[magaz].name}, адрес {shops[magaz].address}.")
    else:
        print("Неверный выбор, попробуйте снова.")













print("Список всех магазинов и товаров:")
for key, shop in shops.items():
    print(f"{key} ({shop.name}, {shop.address}): {shop.list_products() if shop.items else 'Нет товаров'}")
