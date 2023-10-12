import random

height = 17
width = 100

mountain = {
    'x': 0,
    'y': height - 2,
    'padding': 2
}

def getLevelRow():
    return ["'"] * width

level = [getLevelRow() for _ in range(height)]

while mountain['x'] < width:
    randomNumb = random.randint(0, height)
    if randomNumb > mountain['y'] and mountain['y'] < height - mountain['padding']:
        mountain['y'] += 1
        level[mountain['y']][mountain['x']] = '*'
        mountain['x'] += 1
    elif mountain['y'] > mountain['padding']:
        mountain['y'] -= 1
        level[mountain['y']][mountain['x']] = '*'
        mountain['x'] += 1
    




for row in level:
    print(''.join(row))