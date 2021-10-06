import json
from random import sample

with open('places.json', 'r') as file:
    places_dict = json.loads(file.read())

random_text = 'hello world'.upper()

new_text = ''
for char in random_text:
    try:
        new_text += sample(place_dict[char],1)[0]
    except KeyError:
        pass
    new_text += ' '

	
print(new_text)
