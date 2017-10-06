# clip2trello

A program I created for a friend to send the current contents of the Windows
clipboard to a specified Trello list. Loosely based on [this repo.](https://github.com/bmccormack/trello-python-demo)

## Install

1. Download this repo
1. Retrieve your Trello API key and token, save them in settings.py (see below for
  instructions)
1. Download the [paste utility](http://www.c3scripts.com/tutorials/msdos/paste.html)
1. Per the instructions, place paste.exe in `C:\Windows\System32`
1. Set up an AutoHotKey (or similar) shortcut to:
  * Copy the contents of the clipboard to a file using the paste utility
  * Run `main.py` to create the card on the board and list of your choice
  * Remove the file
  * (see `example.ahk` for how to do this)
