# kbdisplay
This is essentially a Python clone of NohBoard which runs on Linux.
Like distplay, I made this because there wasn't any pre-existing
Linux-compatible keyboard input displays that I could find.

Note that this is not multiplatform, this will *only* run on Linux.
If you're on Windows, just use the *real* NohBoard.

This works by reading the output of `xinput test-xi2 --root`, so, y'know,
that's cool. Or maybe not cool. I don't know. I'm not going to say this
is well programmed, because that would probably be a huge lie.

## How to use
Obviously, since this is a Python program, you'll need to first install
Python with your package manager. You will also need to install Tk since that's
what the program is using for its graphical interface.

> 🛈 Note that apparently some Linux distributions don't include the Python
`tkinter` module by default, so you may need to install that seperately; on Ubuntu this
would be the `python3-tk` package.

In order to run this, you need to run `main.py` with one argument,
supplying a layout file. These are json files with a pretty simple
syntax - it shouldn't be too hard to figure it out. For demonstration
purposes, layouts for the default bindings of Distance and Celeste are
included in this repo (in the `layouts` folder). If you want to add more,
fork and submit a PR, or something.

For your convenience, I've included a script, `identify-keys.py`, that
will allow you to find out what keycode each key is mapped to. It's
missing a few of them, and was designed in mind with my UK keyboard,
but it will work for the majority of the keys.
