from PIL import Image, ImageDraw, ImageFont


def add_watermark(image_path, output_path, text="Знак водяной"):
    base_img = Image.open(image_path).convert("RGBA")

    txt_layer = Image.new("RGBA", base_img.size, (255, 255, 255, 0))

    draw = ImageDraw.Draw(txt_layer)

    try:
        font_size = int(base_img.height * 0.05)
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    text_box = draw.textbbox((0, 0), text, font=font)
    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]

    x = base_img.width - text_width - 20
    y = base_img.height - text_height - 20

    draw.text((x, y), text, fill=(255, 255, 255, 128), font=font)

    watermarked = Image.alpha_composite(base_img, txt_layer)

    watermarked.convert("RGB").save(output_path)
    print(f"Знак аддед {image_path} -> сохранен как {output_path}")

images_to_watermark = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

for img_name in images_to_watermark:
    try:
        add_watermark(img_name, f"watermarked_{img_name}", text="© qwer322")
    except FileNotFoundError:
        print(f"Файл {img_name} не найден.")