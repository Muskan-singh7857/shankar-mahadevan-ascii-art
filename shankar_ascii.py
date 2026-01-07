from PIL import Image

img = Image.open("shankar image.jpeg")
img = img.resize((30, 28))   

img = img.convert("L")
chars = " .:-=*#"

def pixel_to_char(pixel):
    index = pixel * len(chars) // 256
    return chars[index]

pixels = img.getdata()
ascii_image = ""

for i, pixel in enumerate(pixels):
    ascii_image += pixel_to_char(pixel)
    if (i + 1) % img.width == 0:
        ascii_image += "\n"

print(ascii_image)

