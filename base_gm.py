from emojis import *
from std_greetings import *
from units_of_time import *
from like_as_with import *
from to_begin import *
from punc import *
import random
BREAD = '<:br3ad:900045472088084510>'

''' base gm'''
def base_gm(general_emojis, standard_greetings, punctuation, to_begin, like_as_with):
    x = random.choice(general_emojis)
    y = random.choice(standard_greetings)
    z = random.choice(punctuation)
    a = random.choice(to_begin)
    b = random.choice(like_as_with)
    output_a = f'{x} {BREAD} {x}'
    output_b = f'{y}, this morning is {x}'
    output_c = f'{y} good morning {BREAD}'
    output_d = f'have a {x} of a day and get {BREAD}'
    output_e = f'{a} today {b} {BREAD}'
    outputs = [output_a, output_b, output_c, output_d, output_e]
    xyz = random.choice(outputs)
    return xyz

if __name__ == "__main__":
    print('--- base reply used ---')
    base_gm(general_emojis, standard_greetings, punctuation, to_begin, like_as_with)
