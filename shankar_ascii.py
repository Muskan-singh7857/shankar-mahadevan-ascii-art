# rows = 22
# cols = 42

# ch = ' '
# ptr = [ch]

# for i in range(rows):
#     for j in range(cols):

#         if i < 4 and 12 < j < 30:
#             ptr[0] = '#'

#         elif 4 < i < 20 and (j == 12 or j == 29):
#             ptr[0] = '|'
            
#         elif i == 8 and (j == 18 or j == 23):
#             ptr[0] = 'o'

#         elif i == 10 and j == 21:
#             ptr[0] = '^'

#         elif 12 <= i <= 16 and 16 < j < 26:
#             ptr[0] = '*'

#         else:
#             ptr[0] = ' '

#         print(ptr[0], end='')
#     print()

# PHOTO TO ASCII FACE (Shankar Mahadevan)
# Paste directly in VS Code and run

# SMALL ASCII PHOTO (Compact like video)

# CLEAN & SMALL ASCII FACE (VIDEO-LIKE OUTPUT)

from PIL import Image

# ---------- LOAD IMAGE ----------
img = Image.open("shankar image.jpeg")

# ---------- RESIZE (IMPORTANT) ----------
img = img.resize((30, 28))   # width x height (terminal friendly)

# ---------- GRAYSCALE ----------
img = img.convert("L")

# ---------- SIMPLE CHARACTER SET ----------
chars = " .:-=*#"

# ---------- PIXEL TO CHAR ----------
def pixel_to_char(pixel):
    index = pixel * len(chars) // 256
    return chars[index]

# ---------- ASCII GENERATION ----------
pixels = img.getdata()
ascii_image = ""

for i, pixel in enumerate(pixels):
    ascii_image += pixel_to_char(pixel)
    if (i + 1) % img.width == 0:
        ascii_image += "\n"

# ---------- OUTPUT ----------
print(ascii_image)

