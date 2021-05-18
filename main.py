import sys
from PIL import Image

# ----------------

debug = False

# ----------------

try:
    sys.argv[1]
except IndexError:
    print("Usage: " + sys.argv[0] + " <filename>")
    exit()

if debug:
    print("Opening image...")
im = Image.open(sys.argv[1])

if debug:
    print("Listing pixels...")
pixels = im.load()
width, height = im.size
asciiMode = False
pyMode = False
pyCode = ""
index = 0
row = 0

if debug:
    print("Parsing pixels...")
for x in range(width):
    row = row + 1
    column = 0

    for y in range(height):
        column = column + 1

        index = index + 1
        pixel = pixels[x, y]

        if debug:
            print("Row " + str(row) + ", column " + str(column) + ", pixel " + str(pixel))

        if pixel == (255, 255, 255):
            if debug:
                print(str(index) + ": ASCII Mode OFF")
            asciiMode = False
        if asciiMode and pixel != (255, 255, 255):
            if debug:
                print(str(index) + ": Processing ASCII")
                continue
            print(chr(pixel[0]), end="")
        if pyMode and pixel != (255, 255, 255):
            if debug:
                print(str(index) + ": Processing Python code")
                continue
            pyCode = pyCode + chr(pixel[0])
        if pixel == (0, 0, 0):
            if debug:
                print(str(index) + ": ASCII Mode ON")
            asciiMode = True
        if pixel == (0, 255, 0):
            if debug:
                print(str(index) + ": Python Mode ON")
            pyMode = True
            pyCode = ""
        if pixel == (0, 0, 255):
            if debug:
                print(str(index) + ": Python Mode OFF")
            pyMode = False
            exec(pyCode.rstrip("\0"))

print("")
