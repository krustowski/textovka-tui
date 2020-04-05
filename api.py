#!/usr/bin/env python3
# encoding: utf-8

import json
import requests

class Api:
    # api vars
    endpoint = "https://text.n0p.cz/" 
    action   = ""
    apikey   = ""
    api      = []
    nickname = ""
    player   = []
    room     = []
    message  = []

    def __init__(self):
        self.getKey()
        self.loadUserData()
    
    def getKey(self):
        # load/fetch apikey
        try:
            with open("./apikey") as f:
                #print("Loading apikey from a file...")
                self.apikey = f.readlines()[0]

        except FileNotFoundError:
            # prompt for nickname
            while True:
                try:
                    nickname = input("Select your nickname: ")
                    if (len(nickname) > 0):
                        break

                except KeyboardInterrupt:
                    print("\n")
                    exit()

            self.nickname = nickname

            # get the JSON from API
            #print("Sending a register call...")
            response = requests.get(self.endpoint + "?register=" + self.nickname)
            data = json.loads(response.text)

            if (data["api"]["status_code"] == 403):
                print("User already exists...")
                exit()

            try:
                f = open("./apikey", "w")
                self.apikey = data["api"]["apikey"]
                f.write(self.apikey)
                f.close()

            except PermissionError:
                print("Check the write permission in this folder...")
                exit()
            
        except PermissionError:
            print("Check the read permission in this folder...")
            exit()

        except IndexError:
            print("Damaged apikey file...")
            exit()

        except IOError:
            print("Generic IO Error...")
            exit()

    def loadUserData(self):
        # get the JSON from API
        #print("Performing a casual API call...")
        response = requests.get(self.endpoint + "?apikey=" + self.apikey)
        data = json.loads(response.text)

        if (data["api"]["status_code"] != 200):
            print("Bad apikey...")
            exit()

        try:
            # load arrays from a registered user
            #print("Loading user data...")
            self.api       = data["api"]
            self.player    = data["player"]
            self.nickname  = data["player"]["nickname"]
            self.room      = data["room"]
            self.message   = data["message"]

        except KeyError:
            print("Invalid JSON data from API...")

    def sendAction(self, action = ""):
        if (action != ""):
            self.action = action

        response = requests.get(self.endpoint + "?apikey=" + self.apikey + "&action=" + self.action)
        data = json.loads(response.text)

        # reload data
        self.api       = data["api"]
        self.player    = data["player"]
        self.nickname  = data["player"]["nickname"]
        self.room      = data["room"]
        self.message   = data["message"]

        return self