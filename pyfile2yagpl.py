import sys
from PIL import Image
from random import randint

try:
    sys.argv[1]
except IndexError:
    print("Usage: " + sys.argv[0] + " <python file>")
    exit()

with open(sys.argv[1], 'r') as f:
    content = f.read()

pixels = [255, 0, 0, 0, 255, 0]

for c in content:
    code = ord(c)
    pixels.append(code)
    pixels.append(randint(1, 254))
    pixels.append(randint(1, 254))

pixels.append(0)
pixels.append(0)
pixels.append(255)

for _ in range(12):
    pixels.append(255)
    pixels.append(0)
    pixels.append(0)

if ((len(pixels)/3) % 2) == 0:
    width = 12
else:
    width = 10

new_image = Image.frombytes("RGB", (int((len(pixels)/3)/width), width), bytes(pixels))
new_image = new_image.rotate(270, expand=True)
new_image = new_image.transpose(Image.FLIP_LEFT_RIGHT)
new_image.save('pyfile2yagpl-output.png')
print("Image exported to 'pyfile2yagpl-output.png'")
