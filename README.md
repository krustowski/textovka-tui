# textovka TUI

python3 TUI for PHP REST API text-based game v1

API endpoint:\
https://text.n0p.cz/

Documentation:\
https://wiki.n0p.cz/doku.php?id=misc:textovka

## Running the TUI

Make sure your python3 environment is all set up first:

```bash
./setup.py
python3 setup.py
```

Then just run the `main.py` script, choose a nickname and start the game!

```bash
./main.py
python3 main.py
```

By performing a registration (script is prompting for a nickname) a new file called `apikey` is created in the actual working directory. 
The file will contain the unique API key used for sending game actions and retrieving the actual player data.

## TUI preview

[tui_started]: img/tui_started.png "TUI started"

[tui_actions]: img/tui_actions.png "TUI map-defined action"

[tui_hp_fall]: img/tui_hp_fall.png "TUI HP fall (drowning)"

[tui_dead]: img/tui_dead.png "TUI after death"
