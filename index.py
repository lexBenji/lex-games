import random
import images
from stuff import *

while True:
    writeln('''
Games: rg,rps
Type "exit" to exit.
''')
    game = input('Choose a game: ').lower()
    if game == 'rg':
        images.generate()
    elif game == 'rps':
        mc = random.choice(['rock','paper','scissors'])
        rps = input('Choose [r,p,s] ').lower()
        if rps == 'r' or rps == 'rock':
            writeln(f'I chose {mc}')
            if mc == 'rock':
                writeln('tie')
            elif mc == 'paper':
                writeln('i lost')
            elif mc == 'scissors':
                writeln('you lost')
        elif rps == 'paper' or rps == 'p':
            writeln(f'I chose {mc}')
            if mc == 'rock':
                writeln('you lost')
            elif mc == 'paper':
                writeln('tie')
            elif mc == 'scissors':
                writeln('i lost')
        elif rps == 's' or rps == 'scissors':
            writeln(f'I chose {mc}')
            if mc == 'rock':
                writeln('you lost')
            elif mc == 'paper':
                writeln('i lost')
            elif mc == 'scissors':
                writeln('tie')
    elif game == 'exit':
        break
