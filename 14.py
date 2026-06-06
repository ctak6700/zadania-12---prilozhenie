import os
from PIL import Image, ImageDraw, ImageFont

def step1_crop_image(input_file, output_file):
    try:
        with Image.open(input_file) as img:
            print(f"Размер изображения: {img.size}")

            crop_box = (50, 50, 500, 400)

            cropped_img = img.crop(crop_box)
            cropped_img.save(output_file)
            print(f"[Найс] Сохранено как '{output_file}'\n")

    except FileNotFoundError:
        print(f"[Ошибка] Файл '{input_file}' не найден. Скачайте другую или переназовите.\n")

def step2_and_3_create_card():
    holidays_dict = {
        "Новый год": "new_yearjpg",
        "День рождения": "birthday.jpg",
    }

    print("Праздники:", ", ".join(holidays_dict.keys()))
    chosen_holiday = input("К какому празднику нужна открытка? ")

    if chosen_holiday not in holidays_dict:
        print("Такого праздника нет в списке.")
        return

    filename = holidays_dict[chosen_holiday]

    try:
        with Image.open(filename) as img:
            img.show()
            recipient = input("Кого хотите поздравить? (введите имя): ")
            greeting_text = f"{recipient}, поздравляю!"

            draw = ImageDraw.Draw(img)
            try:
                font = ImageFont.truetype("arial.ttf", 45)
            except IOError:
                font = ImageFont.load_default()
            bbox = draw.textbbox((0, 0), greeting_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            image_width, image_height = img.size
            y_pos = image_height - text_height - 30
            text_color = "yellow"

            draw.text(
                (x_pos, y_pos),
                greeting_text,
                fill=text_color,
                font=font,
                stroke_width=2,
                stroke_fill="black"
            )
            final_filename = "final_greeting_card.png"
            img.save(final_filename, "PNG")
            print(f"\n[Успех] Итоговая открытка '{final_filename}' сохранена!")
            img.show()

    except FileNotFoundError:
        print(f"[Ошибка] Файл '{filename}' не найден. Скачайте другую или переназовите.")

if __name__ == "__main__":
    print("--- Генератор открыток ---")
    step2_and_3_create_card()