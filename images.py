import random
from stuff import *

def generate():
    generated = []
    z = ''
    for i in range(4):
        for j in range(6):
            z += str(random.randint(0,4))
        generated.append(z)
        z = ''
    writeln('+--------+')
    for i in generated:
        write('| ')
        for j in i:
            if j == '0':
                write(' ')
            elif j == '1':
                write('.')
            elif j == '2':
                write('-')
            elif j == '3':
                write('+')
            elif j == '4':
                write('=')
        write(' |')
        writeln('')
    writeln('+--------+')
