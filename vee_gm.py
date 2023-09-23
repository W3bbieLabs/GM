from like_as_with import *
from to_begin import *
import random
''' emotional ingredients '''
emo_ingredients = [
'patience', 
'empathy', 
'tenacity', 
'candor', 
'gratitude',
'self-awareness',
'accountability',
'optimism',
'empathy',
'curiosity',
'conviction',
'humilty',
'ambition',
]

''' gary vee emo ingredients '''
def vee_gm(emo_ingredients, like_as_with):
	x = random.choice(emo_ingredients)
	y = random.choice(like_as_with)
	z = random.choice(to_begin)
	output_a = f'this morning is perfect {y} **{x}**'
	output_b = f'**make {x} a priority this morning**'
	output_c = f'*{z} today with {x}*'
	output_d = f'**share your {x} with the 🌎 today**'
	outputs = [output_a, output_b, output_c, output_d]
	xyz = random.choice(outputs)
	return f'{xyz.title()}'

if __name__ == "__main__":
	vee_gm(emo_ingredients, like_as_with)