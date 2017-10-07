import requests           # a 3rd party library. I installed via `pip install requests`
import json               # all responses from Trello come back as JSON, so have your favorite JSON library handy
import settings
import os
import sys
import easygui

url = settings.webooks_url

# Absolute path to avoid relative issues
file = open(os.path.join(os.path.dirname(sys.argv[0]), 'paste.txt'), 'r')
copied_data = file.read()

payload = {'text': copied_data}

try:
    requests.post(url, data=json.dumps(payload))
except:
    easygui.msgbox("ERROR: Could not reach webhook. Are you connected to the internet?")
