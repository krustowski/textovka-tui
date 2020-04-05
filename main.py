#!/usr/bin/env python3
# encoding: utf-8

__author__ = "krustowski"
__email__ = "k@n0p.cz"
#__license__ = "MIT"
__date__ = "Sunday, Apr 5, 2020"
__version__ = "1.0"

import npyscreen
from source.tui import textovkaTUI

if __name__ == "__main__":
    #print(api.sendAction().message)
    try:
        textovkaTUI().run()
    except KeyboardInterrupt:
        exit()