import random
import images
from stuff import *

print('Games: rg,rps')

while True:
    game = input('Choose a game: ').lower()
    if game == 'rg':
        images.generate()
    elif game == 'rps':
        mc = random.choice(['rock','paper','scissors'])
        rps = input('Choose [r,p,s] ').lower()
        writeln(f'I chose {mc}')
        if rps == 'r' or rps == 'rock':
            if mc == 'rock':
                writeln('tie')
            elif mc == 'paper':
                writeln('you lost')
            elif mc == 'scissors':
                writeln('i lost')
        elif rps == 'paper' or rps == 'p':
            if mc == 'rock':
                writeln('i lost')
            elif mc == 'paper':
                writeln('tie')
            elif mc == 'scissors':
                writeln('you lost')
        elif rps == 's' or rps == 'scissors':
            if mc == 'rock':
                writeln('you lost')
            elif mc == 'paper':
                writeln('i lost')
            elif mc == 'scissors':
                writeln('tie')
    elif game == 'games' or game == '?' or game == 'h' or game == 'help':
        print('Games: rg,rps')
    elif game == 'exit' or game == 'x':
        break
