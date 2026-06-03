from PIL import Image

img = Image.open('graf fail 1 zadanie.jpg')

new_width = img.width // 3
new_height = img.height // 3

resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

flipped_horizontal = resized_img.transpose(Image.FLIP_LEFT_RIGHT)
flipped_vertical = resized_img.transpose(Image.FLIP_TOP_BOTTOM)

resized_img.save('resiznytaia_kartinka.jpg')
flipped_horizontal.save('horizontal.jpg')
flipped_vertical.save('vertical.jpg')