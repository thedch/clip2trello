; Sample authotkey file for clip2trello

; NOTE: You must modify this script to contain your own paths or it will not work.

^1::
  Send, ^c ; copy the currently selected text
  Run, %comspec% /c C:\Windows\System32\paste.exe > C:\Users\Daniel-SSD\Software\clip2trello\paste.txt
  Run, %comspec% /c C:\Users\Daniel-SSD\AppData\Local\Programs\Python\Python36\python.exe C:\Users\Daniel-SSD\Software\clip2trello\main.py
Return
