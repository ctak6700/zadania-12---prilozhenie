class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean(self):
        print(f"Уборщик {self.name} типа убираеться.")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0.0, cleaner_name="Неизвестный"):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
        self.cleaner = Cleaner(cleaner_name)

    def describe_restaurant(self):
        print(f"Ресторан «{self.restaurant_name}» | Кухня: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан «{self.restaurant_name}» открыт!")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, location, working_hours, flavors=None):
        super().__init__(restaurant_name, cuisine_type)

        self.location = location
        self.working_hours = working_hours

        self.flavors = flavors if flavors else []

        self.types_inventory = {
            "на палочке": [],
            "в стаканчике": [],
            "в рожке": []
        }

    def show_flavors(self):
        print(f"\n Меню вкусов в «{self.restaurant_name}» ")
        if self.flavors:
            print("Сорта: " + ", ".join(self.flavors))
        else:
            print("Мороженого сейчас нет.")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"[+] Сорт '{flavor}' добавлен в меню.")
        else:
            print(f"[!] Сорт '{flavor}' уже в меню.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"[-] Сорт '{flavor}' удален.")
        else:
            print(f"[!] Сорта '{flavor}' нет.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"[?] Да, сорт '{flavor}' есть !")
            return True
        else:
            print(f"[?] Нет, сорта '{flavor}' сейчас нет.")
            return False

    def add_specific_type(self, ice_cream_type, flavor):
        if ice_cream_type not in self.types_inventory:
            self.types_inventory[ice_cream_type] = []

        if flavor not in self.types_inventory[ice_cream_type]:
            self.types_inventory[ice_cream_type].append(flavor)
            print(f"[+] В категорию '{ice_cream_type}' добавлен вкус '{flavor}'.")

    def show_specific_type(self, ice_cream_type):
        if ice_cream_type in self.types_inventory and self.types_inventory[ice_cream_type]:
            flavors_str = ", ".join(self.types_inventory[ice_cream_type])
            print(f"Мороженое типа '{ice_cream_type}': {flavors_str}")
        else:
            print(f"Для типа '{ice_cream_type}' пока нет других вкусов.")




print("ТЕСТ 11.1")
my_ice_cream_stand = IceCreamStand(
    restaurant_name="Смешное мороженное",
    cuisine_type="Кафе-мороженое",
    location="Вознесенский 46, Вознесенский пр., 46, Санкт-Петербург, 190000",
    working_hours="00:00 - 00:00",
    flavors=["Ванильное", "Шоколадное", "Клубничное"]
)

my_ice_cream_stand.show_flavors()




print("\n11.2а")
print(f"Где находимся: {my_ice_cream_stand.location}")
print(f"Время работы: {my_ice_cream_stand.working_hours}")

print("\n11.2б")
my_ice_cream_stand.add_flavor("Фисташковое")
my_ice_cream_stand.add_flavor("Шоколадное")
my_ice_cream_stand.remove_flavor("Ванильное")
my_ice_cream_stand.show_flavors()

print("\n11.2в")
my_ice_cream_stand.check_flavor("Фисташковое")
my_ice_cream_stand.check_flavor("Малиновое")

print("\n11.2г")
my_ice_cream_stand.add_specific_type("на палочке", "Фруктовый лед")
my_ice_cream_stand.add_specific_type("мягкое", "Сливочное")
my_ice_cream_stand.add_specific_type("мягкое", "Шоколадное")
my_ice_cream_stand.add_specific_type("в стаканчике", "Пломбир") 
my_ice_cream_stand.show_specific_type("мягкое")
my_ice_cream_stand.show_specific_type("на палочке")
my_ice_cream_stand.show_specific_type("в стаканчике")

#объединил прошлое задание с этим, был какой то бахлаг я так и не понял че ломалось поэтому объединил
