#!/usr/bin/env python3
# encoding: utf-8

import npyscreen

# ./api.py
from api import Api

# https://npyscreen.readthedocs.io/introduction.html

class App(npyscreen.NPSApp):
        def main(self):
                actions = d.room["actions"] if d.room["actions"] != None else []
                actions.extend(["go-north", "go-south", "go-east", "go-west"])

                inventary = d.player["inventary"]
                # These lines create the form and populate it with widgets.
                # A fairly complex screen in only 8 or so lines of code - a line for each control.
                F   = npyscreen.Form(name = "textovka " + d.api["version"])
                t   = F.add(npyscreen.TitleText, name = "nickname:", value = d.nickname, editable = False)
                s   = F.add(npyscreen.TitleSlider, out_of = 100, label = True, name = "hp", editable = False, value = d.player["hp"])
                ml  = F.add(npyscreen.MultiLineEdit, editable = False,
                #value = """try typing here!\nMutiline text, press ^R to reformat.\n""",
                value = d.message,
                max_height = 4, rely = 9)
                #i  = F.add(npyscreen.TitleSelectOne, editable = False, values = inventary, name = "Inventary")
                ms = F.add(npyscreen.TitleSelectOne, value = [0,], name = "Actions",
                        values = actions, scroll_exit = False)

                # This lets the user interact with the Form.
                F.edit()

                d.sendAction(ms.get_selected_objects()[0])

if __name__ == "__main__":
        d = Api()
        TUI = App()
        TUI.run()