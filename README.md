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

By performing a registration (choosing a nickname) a new file called `apikey` is created in the actual directory. 
The file will contain the unique API key used for sending game actions and retrieving the actual player data.
