# `python-ansi` - ANSI colour code helper for Python

## Overview
*python-ansi* is a Python script I made to help with the printing of **ANSI** terminal colour codes.

## Tf are ansi colour codes
**ANSI** colour codes are a type of escape sequence used for changing the colour, style, and background colour of printed text. **ANSI** colour codes are as follows: `\033` (escape character), `[` (start of colour code), colour code modifiers, then `m`.<br/>
For example, here is an **ANSI** colour code to make text *red*: `\033[31m`<br/>
You can reset the colour and style of the text using `\033[0m`.

## Installation
1. Download the latest version of the *python-ansi* script from the **Releases** tab
2. Copy or Move the script to the location of the python script you want to use *python-ansi* in.

***Alternative Method:***
1. Clone the Git repository:
```
$ git clone https://github.com/ekogii/python-ansi.git /tmp/python-ansi
```
> Note: *You can replace `/tmp/python-ansi` with any other file location if you wish.*

2. Copy or Move the script to the location of the python script you want to use *python-ansi* in:
```
$ cp ansi.py /path/to/desired/location
```

### And you are done with installation!

---

## Usage

The script comes with a class called `ansi`. The constructor takes an argument as a string, which will be modified to change colour / style.<br/>
Example: `ansi( "Test message" )`

This class also has several methods, each to change the colour / style. Each methods returns a copy of the current instance so that you can chain several methods together. Examples:

```python
ansi("Test Message").red() # Change the colour of "Test Message" to red.
ansi("FATAL ERROR!").bold().bright_red() # Makes the message bright red and bolded.
ansi("[Info] ...").white().dim() # Changes the colour to dimmed white.
```

The `ansi` class also has a `__repr__()` method, meaning you can just insert it into a `print()` function to print the coloured text.

```python
print( ansi("example").bold() )
```
Result: **`example`** <-- (bolded text)

---

You can stack as many effect as you want. Observe:

```python
print( ansi("Gocha gocha urusee").bold().italic().bright_white().bg_yellow() )
```

As far as I have tested, the order of the methods doesn't matter, except with `reverse()`, and likely other methods.

