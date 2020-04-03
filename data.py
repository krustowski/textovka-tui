import json
import requests

endpoint = "https://text.n0p.cz/" 
apikey   = ""
action   = ""

# TODO: write file 'apikey' to the actual directory if it is not present, prompt for nickname and perform a register call to API

# load apikey
try:
    with open("./apikey") as f:
        apikey = f.readlines()[0]

except IOError:
    # file not found -> perform a register call
    #print("File not accessible")

    # prompt 
    nickname = "krusty"

    # get the JSON from API
    response = requests.get(endpoint + "?register=" + nickname)
    data = json.loads(response.text)

    if data["api"]["apikey"] == None:
        print("User already exists or API error")
    else:
        # unknown permissions in such dir => unstable approach
        f = open("./apikey", "w")
        f.write(data["api"]["apikey"])
        f.close()

# get the JSON from API
response = requests.get(endpoint + "?apikey=" + apikey + "&action=" + action)
data = json.loads(response.text)

try:
    # load arrays from a registered user
    api     = data["api"]
    player  = data["player"]
    room    = data["room"]
    message = data["message"]

    print(message)

except EnvironmentError as e:
    print("invalid JSON data from API (" + e + ")")