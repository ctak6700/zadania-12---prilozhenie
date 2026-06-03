from PIL import Image

image_path = 'graf fail 1 zadanie.jpg'
img = Image.open(image_path)

img.show()

print("--- Информация об изображении ---")
print(f"Размер (ширина, высота): {img.size} пикселей")
print(f"Формат файла: {img.format}")
print(f"Цветовая модель: {img.mode}")
