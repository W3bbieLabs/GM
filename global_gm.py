from non_us_gm import *
from emojis import *
import random
def global_gm(non_american_gm, general_emojis):
    x = random.choice(non_american_gm)
    y = random.choice(general_emojis) 
    output_a = f'{x}'
    output_b = f'{x} looks foreign yet means good morning {y}'
    outputs = [output_a, output_b]
    xyz = random.choice(outputs)
    return f'{xyz}'

if __name__ == "__main__":
    print('--- using gobal based gm ---')
    global_gm(non_american_gm, general_emojis)