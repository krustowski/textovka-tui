#!/usr/bin/env python3
# encoding: utf-8

__author__ = "krustowski"
__email__ = "k@n0p.cz"
#__license__ = "MIT"
__date__ = "Sunday, Apr 5, 2020"
__version__ = "1.0"

import npyscreen
from source.api import Api

api = Api()

class msgBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLineEdit

class textovkaForm(npyscreen.Form):

    def afterEditing(self):
        # send an action
        a = api.sendAction(self.actions.get_selected_objects()[0])

        # get inventary
        inventary = a.player["inventary"] if a.player["inventary"] != None else []

        # get room actions
        actions = a.room["actions"] if a.room["actions"] != None else []
        actions.extend(["go-north", "go-south", "go-east", "go-west"])

        # update the form
        self.name = "textovka (api: " + a.api["version"] + ") (room: " + a.player["room"] + ")"
        self.hp.value = a.player["hp"]
        self.inventary.values = inventary
        self.message.value = a.message
        self.message.rely = 7 + (len(inventary) - 1 if len(inventary) > 0 else 0)
        #self.actions.max_height = len(actions)
        self.actions.values = actions
        self.actions.value = [0]
        self.actions.rely = 14 + (len(inventary) - 1 if len(inventary) > 0 else 0)# + a.message.count("\n")

        # shall we continue?
        if a.player["game_ended"]:
            self.actions.editable = False
            self.actions.hidden = True

        """
        if a.player["game_ended"]:
            self.parentApp.setNextForm(None)
        else:
            self.parentApp.setNextForm("MAIN")
        """

    def create(self):        
        # get inventary
        inventary = api.player["inventary"] if api.player["inventary"] != None else []

        # get room actions
        actions = api.room["actions"] if api.room["actions"] != None else []
        actions.extend(["go-north", "go-south", "go-east", "go-west"])

        # form objects init
        self.nickname = self.add(npyscreen.TitleText, name = "nickname", editable = False, value = api.player["nickname"])
        self.hp = self.add(npyscreen.TitleSlider, out_of = 100.0, label = True, name = "hp", editable = False, value = api.player["hp"])
        self.inventary = self.add(npyscreen.TitleSelectOne, scroll_exit = True, name = "inventary", values = inventary, rely = 5, editable = False)
        #self.message = self.add(npyscreen.MultiLineEdit, name = "message", value = api.message, editable = False, relx = 18, rely = 8 + (len(inventary) - 1 if len(inventary) > 0 else 0))
        self.message = self.add(msgBox, name = "message", value = api.message, editable = False, relx = 3, rely = 7 + (len(inventary) - 1 if len(inventary) > 0 else 0), max_height = 6, color = "CONTROL")
        self.actions = self.add(npyscreen.TitleSelectOne, scroll_exit = True, max_height = 7, max_width = 0, name = "actions", values = actions, value = [0,], rely = 14 + (len(inventary) - 1 if len(inventary) > 0 else 0))# + api.message.count("\n"))

        # hide the actions, if the game is over
        if api.player["game_ended"]:
            self.actions.editable = False
            self.actions.hidden = True

class textovkaTUI(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", textovkaForm, name = "textovka (api: " + api.api["version"] + ") (room: " + api.player["room"] + ")")