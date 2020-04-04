#!/usr/bin/env python3
# encoding: utf-8

import json
import requests

# api vars
endpoint = "https://text.n0p.cz/" 
apikey   = ""
action   = ""

# load/fetch apikey
try:
    with open("./apikey") as f:
        print("Loading apikey from a file...")
        apikey = f.readlines()[0]

except FileNotFoundError:
    # prompt for nickname
    nickname = "krusty"

    # get the JSON from API
    print("Sending a register call...")
    response = requests.get(endpoint + "?register=" + nickname)
    data = json.loads(response.text)

    if (data["api"]["status_code"] == 403):
        print("User already exists...")
        exit()

    try:
        f = open("./apikey", "w")
        apikey = data["api"]["apikey"]
        f.write(apikey)
        f.close()

    except PermissionError:
        print("Check the write permission in this folder...")
        exit()
    
except PermissionError:
    print("Check the read permission in this folder...")
    exit()

except IOError:
    print("Generic IO Error...")
    exit()

# get the JSON from API
print("Performing a casual API call...")
response = requests.get(endpoint + "?apikey=" + apikey + "&action=" + action)
data = json.loads(response.text)

try:
    # load arrays from a registered user
    print("Loading user data...")
    api     = data["api"]
    player  = data["player"]
    room    = data["room"]
    message = data["message"]

    print(message)

   # ok -> load TUI 

except KeyError:
    print("Invalid JSON data from API...")