import os
import random

place_dict = {
"h" : ["Hungaria" , "Havana"],
"e" : ["Ernakulam" , "Edapally"],
"l" : ["London" , "Los Angeles"],
"o" : ["Ottapalam" , "Olavakode"],
}
msg = "hello"

for element in msg:
	print(place_dict[element][random.randrange(0,len(place_dict[element]))])

