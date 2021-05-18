# Pixhue, a pixel-based programming language

Ever wondered why we don't use images for storing programs? Now it's possible with Pixhue!

> Even though both looks similar, Pixhue is different and incompatible with [Piet](https://www.dangermouse.net/esoteric/piet.html), another pixel-based programming language

## How does it work
You have a JPEG, PNG or [any other image file supported by Pillow](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html), and the image's pixels will be used for instructions.

Every color have a defined instruction (see [Instructions](#Instructions) for more details), and unrecognized colors will be ignored.

## Getting started
First make sure you have Python 3.7 or newer and PIP installed.

* Install the dependancies:
  * ```
    pip install pillow
    ```
* Run any of the [entry points](#Entry-points)

# Entry points
Depending on what you want to do with Pixhue, you can use multiple entry points. If it is the first time you use Python, note that to run a Python file, you need to use this command:
```
python <entry point> [arguments...]
```

| File | Arguments | Description |
--- | --- | ---
|`main.py`|`<filename>`|The Pixhue runtime (to run Pixhue images)|
|`file2yagpl.py`|`<filename>`|Convert a text file to a Pixhue image (ASCII)|
|`str2yagpl.py`|`<text>`|Convert a text string to a Pixhue image (ASCII)|
|`pycode2yagpl.py`|`<code>`|Convert a Python code string to a Pixhue image (Pixhue Python mode)|
|`pyfile2yagpl.py`|`<file>`|Convert a Python file to a Pixhue image (Pixhue Python mode)|

# Instructions
Pixhue files are read like text, from left to right, line by line. If you have a red pixel on pixel `0;0` and a black pixel on pixel `0;1`, the red pixel will be processed first.

Here is the full reference of Pixhue supported instructions. For a detail of how "context" works, go to [Modes](#Modes)

| Example | Code | Context | Description |
--- | --- | --- | ---
|![Red](https://user-images.githubusercontent.com/46352972/118692048-f6d06100-b809-11eb-9bb7-6aacafeba277.png)|HTML: `#ff0000`<br>RGB: `255,0,0`|(any)|Does nothing. Need to be used to fill blank pixels|
|![Black](https://user-images.githubusercontent.com/46352972/118692081-fe900580-b809-11eb-86b1-ba3778937e7e.png)|HTML: `#000000`<br>RGB: `0,0,0`|Normal Mode|Enable ASCII mode (treat the next pixels as ASCII pixels)|
|![Green](https://user-images.githubusercontent.com/46352972/118692099-03ed5000-b80a-11eb-852d-6f09de90dc2d.png)|HTML: `#00ff00`<br>RGB: `0,255,0`|Normal Mode|Enable Python mode (treat the next pixels as ASCII pixels that will be run as Python code)|
|![White](https://user-images.githubusercontent.com/46352972/118692121-08196d80-b80a-11eb-8488-badd2b38689e.png)|HTML: `#ffffff`<br>RGB: `255,255,255`|ASCII Mode|Disable ASCII mode|
|![Blue](https://user-images.githubusercontent.com/46352972/118692143-0cde2180-b80a-11eb-91e5-f69ee0c525d8.png)|HTML: `#0000ff`<br>RGB: `0,0,255`|Python Mode|Disable Python mode (and run code)|
