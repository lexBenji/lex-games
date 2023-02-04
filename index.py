import random
import images
from stuff import *

print('Games: rg,rps')

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
            if mc == 'rock':
                print('tie')
            elif mc == 'paper':
                print('i lost')
            elif mc == 'scissors':
                print('you lost')
        elif rps == 'paper' or rps == 'p':
            if mc == 'rock':
                print('you lost')
            elif mc == 'paper':
                print('tie')
            elif mc == 'scissors':
                print('i lost')
        elif rps == 's' or rps == 'scissors':
            if mc == 'rock':
                print('you lost')
            elif mc == 'paper':
                print('i lost')
            elif mc == 'scissors':
                print('tie')
    elif game == 'exit':
        break
