import npyscreen
from api import Api

class textovkaForm(npyscreen.Form):

    def afterEditing(self):
        # send an action
        a = api.sendAction(self.actions.get_selected_objects()[0])

        # get room actions
        actions = a.room["actions"] if a.room["actions"] != None else []
        actions.extend(["go-north", "go-south", "go-east", "go-west"])

        # get inventary
        inventary = api.player["inventary"] if api.player["inventary"] != None else []

        # update the form
        self.hp.value = a.player["hp"]
        self.inventary.values = inventary
        self.message.value = a.message
        self.message.rely = 7 + len(inventary) - 1
        self.actions.values = actions
        self.actions.value = [0]
        self.actions.max_height = len(actions)
        self.actions.rely = 9 + len(inventary) - 1 + a.message.count("\n")

        # shall we continue?
        if a.player["game_ended"]:
            self.parentApp.setNextForm(None)
        else:
            self.parentApp.setNextForm("MAIN")

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
        self.message = self.add(npyscreen.TitleText, name = "message", value = api.message, editable = False, rely = 7 + len(inventary) - 1)
        self.actions = self.add(npyscreen.TitleSelectOne, scroll_exit = True, max_height = len(actions), name = "actions", values = actions, value = [0], rely = 9 + len(inventary) -1 + api.message.count("\n"))

        # hide the actions, if game is over
        if api.player["game_ended"]:
            self.actions.editable = False
            self.actions.hidden = True

class textovkaTUI(npyscreen.NPSAppManaged):
   def onStart(self):
       self.addForm("MAIN", textovkaForm, name = "textovka " + str(api.api["version"]))

if __name__ == "__main__":
    api = Api()
    #print(api.sendAction().message)
    try:
        textovkaTUI().run()
    except KeyboardInterrupt:
        exit()