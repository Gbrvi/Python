from random import choice
from termcolor import colored

num = 15
cores = ('red', 'yellow', 'blue', 'white', 'magenta', 'grey', 'cyan', 'green')


def tree():

    for n in range(num): 
        print(' '*(num-n), end='') 

        if n == 0:
            print('★')

        if n > 0:
            print(colored(f'{" —" * n }', choice(cores)))
        
    for c in (range(2)):
        print(' ' * (num - 1), end='')

        print(f'{"| |"}')
    

tree()





        