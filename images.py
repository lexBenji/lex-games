import random

img = []
z = ''

for i in range(6):
    for j in range(8):
        z += str(random.randint(1,5))
    img.append(z)
    z = ''
