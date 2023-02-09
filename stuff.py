def write(*text):
    st = ''
    for i in text:
        st += str(i)
        print(st,end='')

def writeln(*text):
    st = ''
    for i in text:
        st += str(i)
        print(st)
