import os
from PIL import Image, ImageFilter

files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
output_dir = 'filtered_images'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file_name in files:
    try:
        img = Image.open(file_name)
        filtered_img = img.filter(ImageFilter.CONTOUR)
        new_path = os.path.join(output_dir, f"filtered_{file_name}")
        filtered_img.save(new_path)
        print(f"Файл {file_name} успешно сохранен в {new_path}")

    except FileNotFoundError:
        print(f"Ошибка: Файл {file_name} нет в папке. ")