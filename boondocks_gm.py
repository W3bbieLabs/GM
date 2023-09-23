from boondocks_char import*
import random
''' boondocks gm'''
def boondocks_gm (boondocks_characters):
    vowels = ('a','e','i','o','u')
    x = random.choice(boondocks_characters)
    print('--- resolving a/an issues ---')
    for v in vowels:
        if x.startswith(v):
            output_a = f'have an {x} morning'
            output_b = f'it is an {x} morning'
        else:
            output_a = f'have a {x} morning'
            output_b = f'it is a {x} morning'
    print('--- resolved a/an issues ---')
    output_c = f'**good morning - from *{x}***'
    output_d = f'*{x}* says good morning'
    outputs = [output_a, output_b, output_c, output_d]
    xyz = random.choice(outputs)
    return f'{xyz}'
if __name__ == "__main__":
	print('--- boondocks gm used ---')
	boondocks_gm (boondocks_characters)
