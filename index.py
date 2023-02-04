import images
from stuff import *

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
