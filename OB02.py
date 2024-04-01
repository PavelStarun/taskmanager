class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access = "Пользователь"

    def get_user(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access(self):
        return self._access

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access = "Админ"
        self._user_list = []

    def add_user(self, user):
        self._user_list.append(user)
        print(f"Сотрудник {user.get_name()} был добавлен в список.")

    def remove_user(self, user):
        self._user_list.remove(user)
        print(f"Сотрудник {user.get_name()} был удален из списка.")

    def get_user_list(self):
        return self._user_list


users = []
admin = Admin(325, "Петр")
user1 = User(111, "Павел")
user2 = User(192, "Марина")
user3 = User(299, "Анастасия")
user4 = Admin(231, "Александр")
user5 = User(119, "Василий")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)
admin.add_user(user4)
admin.add_user(user5)


admin.set_name("Маргарита")

admin.remove_user(user1)

print(user5.get_name())

user_list = admin.get_user_list()
print("Список сотрудников:")
for user in user_list:
    print(f"ID: {user.get_user()}, Имя: {user.get_name()}, Доступ: {user.get_access()}")