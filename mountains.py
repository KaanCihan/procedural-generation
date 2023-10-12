import random
import time
import math

height = 15
width = 100

mountain = {
    'x': 0,
    'y': int(random.randint(0,14)),
    'padding': 2
}

cloud = {
    'x': int(random.randint(0, width)),
    'y': int(random.randint(0, 5)),
    'paddingUp': 1,
    'paddingDown': 13,
    'cloudSize': 200,
    'cloudCount' : int(random.randint(2, 6))
}

clouds = []
cloudSize = cloud['cloudSize']

for _ in range(cloud['cloudCount']):
    cloudy = random.randint(0, cloud['cloudSize'])
    cloudSize -= cloudy
    clouds.append(cloudy)

def getLevelRow():
    return [" "] * width

level = [getLevelRow() for _ in range(height)]

while mountain['x'] < width:
    randomNumb = random.randint(0, height)
    if randomNumb > mountain['y'] and mountain['y'] < height - 1 - mountain['padding']:
        mountain['y'] += 1
        for column in range(mountain['y'], height):
            level[column][mountain['x']] = '#'
        mountain['x'] += 1
    elif mountain['y'] > mountain['padding'] + 1:
        mountain['y'] -= 1
        for column in range(mountain['y'], height):
            level[column][mountain['x']] = '#'
        mountain['x'] += 1


while cloud['cloudCount'] > 0:
    cloud['x'] = int(random.randint(0, width))
    cloud['y'] = int(random.randint(0, 5))
    
    cloudWidth = random.randint(3,5)
    cloudHeight = 3

    if 0 <= cloud['y'] + 1 < height and 0 <= cloud['x'] + cloudWidth < width: 
        level[cloud['y'] + 1][cloud['x'] + cloudWidth] = 'o'
    if 0 <= cloud['y'] + 1 < height and 0 <= cloud['x'] - 1 < width:
        level[cloud['y'] + 1][cloud['x'] - 1] = 'o'
    for i in range(cloudHeight):
        for j in range(cloudWidth):
            row_index = cloud['y'] + i
            col_index = cloud['x'] + j
            if 0 <= row_index < height and 0 <= col_index < width:
                if level[row_index][col_index] == ' ':
                    level[row_index][col_index] = 'o'
        
    cloud['cloudCount'] -= 1


'''cloudSizee = 0
cloudNumber = 0
while cloud['cloudSize'] >= 0:
    
    if level[cloud['y']][cloud['x']] == ' ':
        level[cloud['y']][cloud['x']] = 'o'
        cloud['cloudSize'] -= 1
        cloudSizee += 1
    elif level[cloud['y']][cloud['x']] == '#':
        cloud['cloudSize'] -= 1
        cloudSizee += 1
    
            
    randomint = random.randint(1,4)

    if randomint == 1 and cloud['x'] >= 0:
        cloud['x'] -= 1
    elif randomint == 2 and cloud['x'] < width - 1:
        cloud['x'] += 1  
    elif randomint == 3 and cloud['y'] >= cloud['paddingDown']:
        cloud['y'] -= 1
    elif randomint == 4 and cloud['y'] < height - cloud['paddingUp']:
        cloud['y'] += 1

    if cloudSizee == clouds[cloudNumber]:
        cloud['x'] = int(random.randint(0, width))
        cloud['y'] = int(random.randint(0, 5))
        cloudNumber += 1
    '''
    

for row in level:
    print(''.join(row))