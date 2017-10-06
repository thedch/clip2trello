; Sample authotkey file for clip2trello

; NOTE: Currently, the paste files MUST be stored in the same directory as the
; main.py file

^1::
  Send, ^c ; copy the currently selected text
  Run, %comspec% /c C:\Windows\System32\paste.exe > \path\to\paste\file\in\settings.py
  Run, %comspec% /c \path\to\python.exe \path\to\main.py
  Run, %comspec% /c del /f \path\to\file\in\settings.py
Return
