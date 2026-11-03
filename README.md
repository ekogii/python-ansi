# `python-ansi` - ANSI colour code helper for Python

## Overview
`python-ansi` is a Python script I made to help with the printing of **ANSI** terminal colour codes.

## Tf are ansi colour codes
**ANSI** colour codes are a type of escape sequence used for changing the colour, style, and background colour of printed text. **ANSI** colour codes are as follows: `\033` (escape character), `[` (start of colour code), colour code modifiers, then `m`.<br/>
For example, here is an **ANSI** colour code to make text *red*: `\033[31m`<br/>
You can reset the colour and style of the text using `\033[0m`.

## Installation
1. Download the latest version of the `python-ansi` script from the [releases tab](https://github.com/ekogii/python-ansi/releases).
2. Copy or Move the script to the location of the python script you want to use *python-ansi* in.

***Alternative Method:***
1. Clone the Git repository:
```
$ git clone https://github.com/ekogii/python-ansi.git /tmp/python-ansi
```
> Note: *You can replace `/tmp/python-ansi` with any other file location if you wish.*

2. Copy or Move the script to the location of the python script you want to use *python-ansi* in:
```
$ cp /tmp/python-ansi/ansi.py /path/to/desired/location
```

### And you are done with installation!

---

## Usage

The script comes with a class called `ansi`. The constructor takes an argument as a string, which will be modified to change colour / style.<br/>
Example: `ansi( "Test message" )`

This class also has several methods, each to change the colour / style. Each methods returns a copy of the current instance so that you can chain several methods together.<br/>
Examples:

```python
ansi("Test Message").green() # Change the colour of "Test Message" to green.
ansi("FATAL ERROR!").bold().bright_red() # Makes the message bright red and bolded.
ansi("[Info] ...").white().dim() # Changes the colour to dimmed white.
```

The `ansi` class also has a `__repr__`, meaning you can just insert it into a `print()` function to print the modified text.<br/>Example:

```python
print( ansi("example").bold().cyan() )
```

---

You can stack as many effect as you want. Observe:

```python
print( ansi("gocha gocha urusee").bold().italic().bright_white().bg_yellow() )
```

As far as has been tested, the order the methods are called does not matter, aside from `reverse()` where you have to apply foreground and background colours <u>before</u> calling it.

---
### Basic Effects *(# 0-5 and 7-9)*
**ANSI** codes *0-5* and *7-9* control text effects, (not colour) like making text **bold**, *italic*, or <u>underlined</u>.

Methods for text effects in order:
```python
#0-5
none() # Reset text colours and effects
bold() # Makes text bold
dim() # Dims text colour
italic() # Makes text italic
underline() # Underlines text
blink() # Makes text blink in sync with the text cursor

#7-9
reverse() # Swaps foreground and background colours
hide() # Hides text, useful for when entering passwords or smt idk
strikethrough() # Makes text strikethrough
```

---
### Basic foreground colours *(# 30-37 and 90-97)*
**ANSI** codes *30-37* and *90-97* control basic foreground colours. *30-37* are regular brightness colours, and *90-97* are bright colours.

Methods for foreground colours in order:
```python
#30-37      #90-97
black()     bright_black()
red()       bright_red()
green()     bright_green()
yellow()    bright_yellow
blue()      bright_blue()
magenta()   bright_magenta
cyan()      bright_cyan()
white()     bright_white()
```

---
### Basic background colours *(# 40-47)*
**ANSI** codes *40-47* control basic text background\* / colours.
> \*Note that this does not change the whole terminal background colour, only the background behind the text.<br/>


Methods for background colours in order:
```python
#40-47
bg_black()
bg_red()
bg_green()
bg_yellow()
bg_blue()
bg_magenta()
bg_cyan()
bg_white()
```

---
### 256-colour text colouring
`python-ansi` supports 256-colour foreground <u>and</u> background colouring.<br/>
To utilize this, `python-ansi` comes with two methods for foreground and background 256-colour support.

```python
# 256-colour foreground
# Takes an integer as an argument where 0 <= n <= 255
fg_256( n )

# 256-colour background
# Takes an integer as an argument where 0 <= n <= 255
bg_256( n )
```

---
### 24-bit true colour
`python-ansi` also supports 24-bit *"true colour"* through the `fg_true_colour()` and `bg_true_colour()` methods. These allow you to colour text using values 0-255 for red, green, and blue individually.

> *While many modern terminal emulators support 24-bit true colour, some older terminals may not support it. In many situations it's likely better to just use 256-colour as opposed to 24-bit. Please keep this in mind when using 24-bit colour.*

```python
# 24-bit foreground colour
# Takes 3 integers as arguments, each where 0 <= n <= 255
fg_256( r, g, b )

# 24-bit background colour
# Takes 3 integers as arguments, each where 0 <= n <= 255
bg_256( r, g, b )
```

---
### Aliases for methods
Some methods have aliases for easier typing.

The full list is as follows:
```
     ALIAS                  ORIGINAL
===============     ========================
reset()             none()
strike()            strikethrough()

pink()              magenta()
bg_pink()           bg_magenta()
bright_pink()       bright_magenta()

fg_24b(r, g, b)     fg_true_colour(r, g, b)
bg_24b(r, g, b)     bg_true_colour(r, g, b)
```
