import random
import images
from stuff import *

writeln('Games: rg,rps')

while True:
    game = input('Choose a game: ').lower()
    if game == 'rg':
        writeln('+----------+')
        for i in images.img:
            write('| ')
            for j in i:
                if j == '0':
                    write(' ')
                elif j == '1':
                    write('-')
                elif j == '2':
                    write('~')
                elif j == '3':
                    write('%')
                elif j == '4':
                    write('@')
                elif j == '5':
                    write('#')
            write(' |')
            writeln('')
        writeln('+----------+')
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
