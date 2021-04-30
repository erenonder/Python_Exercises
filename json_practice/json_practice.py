import json


with open("states.json", 'r') as json_file:
    data = json.load(json_file)


states = data['states']


for state in states:
    del state['area_codes']


with open("states_modified.json", 'w') as json_file:
    json.dump(states, json_file, indent=2)
