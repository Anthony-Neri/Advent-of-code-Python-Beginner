def extract_data_file(file):

    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2024_12.txt"


field = extract_data_file(file)

field=[list(line ) for line in field]


farming ={}

for y in range(len(field)):
    for x in range(len(field[y])):
        farmingType = field[y][x] 
        if farmingType in farming:
            farming[farmingType].append((y, x))
        else:
            farming[farmingType] = [(y, x)]


def getZone(start, positions_set):
    stack = [start]
    zone = {start}

    while stack:
        y, x = stack.pop()
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            n = (y + dy, x + dx)
            if n in positions_set and n not in zone:
                zone.add(n) 
                stack.append(n) 

    return zone



                




regionFarming = {}
region = 0

for farmingType, positions in farming.items():
    positions = set(positions)

    while positions:
        start = next(iter(positions))
        zone = getZone(start, positions)
        positions -= zone
        regionFarming[(farmingType, region)] = zone
        region += 1

    
priceFences=0
for region,positions in regionFarming.items():
    nbrFences = 0
    
    nbrPositions = len(positions)
    positions= set(positions)

    for position in positions:
        y,x = position
        fences = 4
        for dy, dx in [(1,0), (-1,0), (0,1), (0,-1)]:
            n = (y + dy, x + dx)
            if n in positions:
                fences-=1
        
        nbrFences+=fences
    
    priceFences+= nbrFences*nbrPositions

print(priceFences)
