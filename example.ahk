; Sample authotkey file for clip2trello

^1::
  Send, ^c ; copy the currently selected text
  Run, %comspec% /c \path\to\paste.exe > \path\to\file\in\settings.py
  Run, %comspec% /c \path\to\python.exe \path\to\main.py
  Run, %comspec% /c del /f \path\to\file\in\settings.py
Return
