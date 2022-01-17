#!/usr/bin/env python3
# encoding: utf-8

__author__ = "krustowski"
__email__ = "k@n0p.cz"
__license__ = "MIT"
__date__ = "Sunday, Apr 5, 2020"
__version__ = "1.0"

try:
    import npyscreen
    import requests
    import signal
except:
    print("Run './setup.py install' first...")
    exit()

from source.tui import textovkaTUI

endpoint = "https://text.n0p.cz/"
TUI = None

def reloadTUI(signalNumber, frame):
    try:
        # destroy TUI (nasty way...)
        TUI.exitApplication()

        # render new TUI
        TUI = textovkaTUI()
        TUI.run()
    except KeyboardInterrupt:
        TUI.exitApplication()

if __name__ == "__main__":
    try:
        TUI = textovkaTUI()
        TUI.run()
    
        # catch UNIX SIGWINCH (terminal window size changed)
        signal.signal(signal.SIGWINCH, reloadTUI)
    except KeyboardInterrupt:
        TUI.exitApplication()

