from emojis import *
from units_of_time import *
from like_as_with import *
from emo_ingredients import *
from clocks import *
import random
def time_gm(units_of_time, like_as_with, general_emojis, emo_ingredients):
    x = random.choice(units_of_time)
    y = random.choice(like_as_with)
    z = random.randrange(2,9999)
    a = random.choice(general_emojis)
    b = random.choice(emo_ingredients)
    c = random.choice(clocks)
    output_a =  f'the first {z} {x} of this morning are yours'
    output_b = f'this morning happened in {z} {x} {a}'
    output_c = f'{c} |  {a} : {random.choice(general_emojis)}{random.choice(general_emojis)}'
    outputs = [ output_a, output_b, output_c ]
    xyz = random.choice(outputs)
    print(f'newest update: {output_c}')
    return f'{xyz}'
if __name__ == "__main__":
    print('--- using time based gm reply ---')
    time_gm(units_of_time, like_as_with, general_emojis, emo_ingredients)