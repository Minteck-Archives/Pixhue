import sys, logging, json
from PIL import Image

# ----------------

debug = False

# ----------------

logging.basicConfig(filename='./yagpl.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

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
global programStack
programStack = []

if debug:
    print("Parsing pixels...")
for x in range(width):
    row = row + 1
    column = 0

    for y in range(height):
        try:
            column = column + 1

            index = index + 1
            pixel = pixels[x, y]

            try:
                lcSet
                lineComment = True
            except NameError:
                lineComment = False

            if debug:
                print("Row " + str(row) + ", column " + str(column) + ", pixel " + str(pixel))

            # General Operators
            if not lineComment and pixel == (255, 255, 255):
                if debug:
                    print(str(index) + ": ASCII Mode OFF")
                asciiMode = False
            if not lineComment and pixel == (255, 0, 255):
                if debug:
                    print(str(index) + ": Starting Line Comment")
                lcSet = True
                continue
            if not lineComment and asciiMode and pixel != (255, 255, 255):
                if debug:
                    print(str(index) + ": Processing ASCII")
                print(chr(pixel[0]), end="")
            if not lineComment and pixel == (255, 0, 0):
                if debug:
                    print(str(index) + ": Blank Pixel")
                continue
            if not lineComment and pyMode and pixel != (255, 255, 255):
                if debug:
                    print(str(index) + ": Processing Python code")
                pyCode = pyCode + chr(pixel[0])
            if not lineComment and not pyMode and pixel == (0, 0, 0):
                if debug:
                    print(str(index) + ": ASCII Mode ON")
                asciiMode = True
            if not lineComment and not asciiMode and pixel == (0, 255, 0):
                if debug:
                    print(str(index) + ": Python Mode ON")
                pyMode = True
                pyCode = ""
            if not lineComment and pixel == (0, 0, 255):
                if debug:
                    print(str(index) + ": Python Mode OFF")
                pyMode = False
                exec(pyCode.rstrip("\0"))

            # Stack Management
            if not lineComment and not pyMode and not asciiMode and pixel == (127, 0, 0):
                if debug:
                    print(str(index) + ": Dumping Stack")
                print("STKD: Stack Dump:")
                for i in programStack:
                    print("    :" + str(i))
                if len(programStack) < 1:
                    print("    :<EMPT: Empty>")
            if not lineComment and not pyMode and not asciiMode and pixel == (0, 0, 127):
                if debug:
                    print(str(index) + ": Flushing Stack")
                programStack = []

            # Stack Length Checker
            if len(json.dumps(programStack)) > 2048: # Workaround here because for some reason using len(bytes(programStack)) just doesn't work
                print("STKO: Stack Overflow")
                quit()
        except KeyboardInterrupt as err:
            print("SEGV: Segmentation Fault")
            logger.error(err)
            print(err)
            quit()

if len(programStack) > 0:
    print("MNEF: Memory Not Emptied Fault")
    quit()

print("SEC0: Successfully Exited")
