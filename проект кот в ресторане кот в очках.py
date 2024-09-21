from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")
top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")
print("Список картинок: ")
print("1.Кот в ресторане")
print("2. Кот в очках")
image_number = int(input("Введите номер картинки: "))
if image_number == 1:
    image = "Кот в ресторане.png"
elif image_number == 2:
    image = "Кот в очках.png"
image = Image.open(image)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size=70)
widht, height = image.size
text = draw.textbbox((0, 0), top_text, font)
text2 = text[2]
draw.text(((widht-text2)/2, 10), top_text, font = font, fill = "black")
text = draw.textbbox((0, 0), bottom_text, font)
text2 = text[2]
text3 = text[3]
draw.text(((widht-text2)/2, height-text3-10), bottom_text, font = font, fill = "black")
image.save("mem.jpg")
