import requests           # a 3rd party library. I installed via `pip install requests`
import json               # all responses from Trello come back as JSON, so have your favorite JSON library handy
from pprint import pprint # this is a handy utility for printing dictionaries in a human readable way
import settings

key = settings.trello_key
token = settings.trello_token
board_name = settings.board_name
list_name = settings.list_name

base = 'https://trello.com/1/'

# Create the URL based on the documentation
boards_url = base + 'members/me/boards'

# Store the API key and token as parameters
params_key_and_token = {'key':key,'token':token}

# Since we only want the name of the board, let's supply the 'fields' argument
# as well. We're also going to ask for lists, to be used later.
arguments = {'fields': 'name', 'lists': 'all'}

response = requests.get(boards_url, params=params_key_and_token, data=arguments)

# The following will give us an array of dictionaries
response_array_of_dict = response.json()

# Find the ID of the desired board
for board in response_array_of_dict:
  if board['name'] == board_name:
    board_id = board['id']

lists_url = base + 'boards/' + board_id + '/lists'
response = requests.get(lists_url, params=params_key_and_token)
response_array_of_dict = response.json()

# Find the ID of the desired list
for trello_list in response_array_of_dict:
  if trello_list['name'] == list_name:
    list_id = trello_list['id']

file = open('paste.txt', 'r')
name = file.read()

# name = 'Card via the API'
description = 'I made this card using the Trello API :fist:'
cards_url = base + 'cards'

arguments = {'name': name,
             'desc': description,
             'idList' : list_id}

response = requests.post(cards_url, params=params_key_and_token, data=arguments)
