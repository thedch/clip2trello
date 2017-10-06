import requests           # a 3rd party library. I installed via `pip install requests`
import json               # all responses from Trello come back as JSON, so have your favorite JSON library handy
from pprint import pprint # this is a handy utility for printing dictionaries in a human readable way


key = ''
# if you're storing your key in this file, you don't need the following three lines
if not key:
  from settings import trello_key
  key = trello_key

token = ''
# if you're storing your token in this file, you don't need the following three lines
if not token:
  from settings import trello_token
  token = trello_token

base = 'https://trello.com/1/'

# Build out the URL based on the documentation
boards_url = base + 'members/me/boards'

# Let's store our API key and token as parameters
params_key_and_token = {'key':key,'token':token}

# Since we only want the name of the board, let's supply the 'fields' argument as well. We're also going to
# ask for lists, to be used later.
arguments = {'fields': 'name', 'lists': 'all'}

# The requests library has separate methods for get, put, post, and delete. We need a GET here.
# We need to provide the URL we want to access, the key and token (params_key_and_token) as params, as well as
# any arguments (arguments) as data.
response = requests.get(boards_url, params=params_key_and_token, data=arguments)

# The following will give us an array of dictionaries
response_array_of_dict = response.json()
# print response_array_of_dict
# Let's go ahead and iterate through the list of boards and print the name of each board
for board in response_array_of_dict:
  if board['name'] == 'Welcome Board':
    board_id = board['id']

lists_url = base + 'boards/' + board_id + '/lists'
response = requests.get(lists_url, params=params_key_and_token)
response_array_of_dict = response.json()
list_id = response_array_of_dict[0]['id']

# TODO Create the card based on data from a file
name = 'Card via the API'
description = 'I made this card using the Trello API :fist:'
cards_url = base + 'cards'

arguments = {'name': name,
             'desc': description,
             'idList' : list_id}

response = requests.post(cards_url, params=params_key_and_token, data=arguments)

pprint(response.json())
