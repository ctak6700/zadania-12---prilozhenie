class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean(self):
        print(f"Уборщик {self.name} убираеться.")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=9.9, cleaner_name="Неизвестный"):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

        self.rating = rating

        self.cleaner = Cleaner(cleaner_name)

    def describe_restaurant(self):
        print(f"Ресторан «{self.restaurant_name}» | Кухня: {self.cuisine_type} | Текущий рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан «{self.restaurant_name}» открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана «{self.restaurant_name}» успешно обновлен до {self.rating}.")

    def start_cleaning(self):
        print(f"[Менеджер]: Навести порядок в «{self.restaurant_name}»!")
        self.cleaner.clean()

print("10.1")
newRestaurant = Restaurant("Denchick Bondarev", "Питерская", cleaner_name="Rhenjq nbg")

print(f"Название: {newRestaurant.restaurant_name}")
print(f"Тип кухни: {newRestaurant.cuisine_type}")

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

print("\n10.2")
restaurant_1 = Restaurant("Buldak", "Японская")
restaurant_2 = Restaurant("Вкусно и точка", "Русская")
restaurant_3 = Restaurant("Все по 250", "Грузинская")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print("\n10.3")
restaurant_1.describe_restaurant()
restaurant_1.update_rating(4.8)
restaurant_1.describe_restaurant()

print("\n10.4")
newRestaurant.start_cleaning()

#все что у меня получилось