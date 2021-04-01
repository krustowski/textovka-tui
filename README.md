# textovka TUI

python3.7 TUI client for PHP REST API text-based game v1

API endpoint:\
https://text.n0p.cz/

API documentation:\
https://github.com/krustowski/textovka-api

## Running the TUI

### Docker

Just install docker engine, clone this repo and run the project:
```bash
make run
```

### Other (legacy)

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

When successfully registred, the initial room properties are loaded and shown on screen (no `ping` info at this moment):

![_][tui_started]

In every room, all four default actions (directions) are available even though they do not have to be implemented in the map ("There is no such way in this room."). Actions can be map-defined, here `climb-up` action is loaded from the map:

![_][tui_actions]

It is also possible to define trap rooms like `well` room in the figure below. One is stuck in there, drowning and dying -> `hp` fall:

![_][tui_hp_fall]

After death (`hp` = 0), one is not able to continue and has to quit the game (Control-C is a possible way to exit the TUI).

![_][tui_dead]
