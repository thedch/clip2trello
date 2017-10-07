# clip2trello

A program I created for a friend to send the current contents of the Windows
clipboard to a specified Trello list. Some Trello API code inspired by
[this repo.](https://github.com/bmccormack/trello-python-demo)

## Install

1. Download this repo
1. Retrieve your [Trello API key and token](https://trello.com/1/appKey/generate), save them in `settings.py`
1. Download this [paste utility](http://www.c3scripts.com/tutorials/msdos/paste.html)
1. Per the instructions at that link, place paste.exe in `C:\Windows\System32`
1. Download the latest [Python 3](https://www.python.org/downloads/) if you
  don't have it already
1. Remember where you installed `python.exe`, you'll need it for the next step
1. Modify the included example.ahk to reflect your system.
    1. Change the path to `paste.txt`
    1. Change the path to `main.py` (needs to be the same path as paste.txt)
    1. Change the path to `python.exe` (on Windows, it should be similar to mine)
    1. Change the trigger from `Ctrl+1` to whatever is most convenient
