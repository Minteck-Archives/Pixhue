# Pixhue, a pixel-based programming language

Ever wondered why we don't use images for storing programs? Now it's possible with Pixhue!

## How does it work
You have a JPEG, PNG or [any other image file supported by Pillow](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html), and the image's pixels will be used for instructions.

Every color have a defined instruction (see [Instructions](#Instructions)) for more details, and unrecognized colors will be ignored.

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

Here is the full reference of Pixhue supported instructions:

| Color | Context | Description |
--- | --- | ---
|a|(any)|Does nothing. Need to be used to fill blank pixels|
|b|No mode|Enable ASCII mode (treat the next pixels as ASCII pixels)|
|c|No mode|Enable Python mode (treat the next pixels as ASCII pixels that will be run as Python code)|
|d|ASCII Mode|Disable ASCII mode|
|e|Python Mode|Disable Python mode (and run code)|