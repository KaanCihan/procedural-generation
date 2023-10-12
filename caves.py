import random
 
width = 95
height = 35
 
land = {
    'landSize': 1000,
    'padding': 2,
    'x': int(width/2),
    'y': int(height/2),
    'landCount': random.randint(3,6)
}
 
def getLevelRow():
    return [' '] * width
lands = []
landSize = land['landSize']

for _ in range(land['landCount']):
    y = random.randint(0, landSize)
    landSize -= y 
    lands.append(y)

random.shuffle(lands)

print(lands)


level = [getLevelRow() for _ in range(height)]

landNumber = 0
landSizee = 0
while land['landCount'] >= 0:
    x = land['x']
    y = land['y']
    
    if level[y][x] == ' ':
        level[y][x] = '#'
        landSizee += 1
    
    roll = random.randint(1, 4)
    
    if roll == 1 and x > land['padding']:
        land['x'] -= 1
    
    if roll == 2 and x < width - 1 - land['padding']:
        land['x'] += 1
    
    if roll == 3 and y > land['padding']:
        land['y'] -= 1
    
    if roll == 4 and y < height - 1 - land['padding']:
        land['y'] += 1

    print(y, x)
    if landSizee == lands[landNumber]:
        landNumber += 1
        land['landCount'] -= 1
        while level[y][x] == '#': 
            x = random.randint(2, width)
            y = random.randint(2, height)
            print(landSizee)
    

    
        
 
for row in level:
    print( ''.join(row) )