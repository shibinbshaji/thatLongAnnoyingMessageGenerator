import pyfiglet
import argparse
import json
from random import sample


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--Stealth",help = "Open without Banner",action='store_true')
parser.add_argument("-m", "--Message", help = "Insert Text")

# Read arguments from command line
args = parser.parse_args()

if (args.Stealth == False):
	result = pyfiglet.figlet_format("lul", font = "isometric1" )
	print(result)
else:
	print("lul")

with open('places.json', 'r') as file:
    places_dict = json.loads(file.read())

random_text = args.Message.upper()
##random_text = 'hello world'.upper()

##print(random_text)
##print(type(random_text))

new_text = ''
for char in random_text:
    try:
        new_text += sample(places_dict[char],1)[0]
    except KeyError:
        pass
    new_text += ' '
	
print(new_text)
