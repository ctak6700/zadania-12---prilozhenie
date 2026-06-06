import json

with open('products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data['products']:
    print(f"Название: {item['name']}")
    print(f"Цена: {item['price']}")
    print(f"Вес: {item['weight']}")
    print("В наличии\n" if item['available'] else "Нет в наличии!\n")