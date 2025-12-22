from collections import defaultdict

def extract_data_file(file):

    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    

def get_contiguous_cells(start_cell, all_cells, directions):
    stack = [start_cell]
    region_cells = {start_cell}

    while stack:
        y, x = stack.pop() 
        for dy, dx in directions:
            neighbor = (y + dy, x + dx)
            if neighbor in all_cells and neighbor not in region_cells:
                region_cells.add(neighbor) 
                stack.append(neighbor)

    return region_cells


def count_contiguous_fences(fences, direction):
    count = 0
    while fences :
        start_cell = next(iter(fences))

        contiguous_fences = get_contiguous_cells(start_cell,fences,direction)

        fences -= contiguous_fences
        count+=1
    
    return count


file = "data/2024_12.txt"

field = extract_data_file(file)

field=[list(line) for line in field]


farming_by_type = defaultdict(set) # Crée la clé de type set si non présente
for y, row in enumerate(field):
    for x, type in enumerate(row):
        farming_by_type[type].add((y, x))




HORIZONTAL = [(0,1), (0,-1)]
VERTICAL = [(1,0), (-1,0)]
ALL = HORIZONTAL + VERTICAL

region_farming = {}
region = 0

for plant_type, positions in farming_by_type.items():

    while positions:
        start = next(iter(positions))
        zone = get_contiguous_cells(start, positions, ALL)
        positions -= zone
        region_farming[(plant_type, region)] = zone
        region += 1

    
total_price=0

for region,positions in region_farming.items():

    fences = {
    "top": set(),
    "bottom": set(),
    "left": set(),
    "right": set(),
    }

    side_count = 0
    area = len(positions)
    positions= set(positions)

    for position in positions:
        y,x = position

        if (y+1,x) not in positions:
            fences["top"].add(position)
        
        if (y-1,x) not in positions:
            fences["bottom"].add(position)
        
        if (y,x+1) not in positions:
            fences["right"].add(position)
        
        if (y,x-1) not in positions :
            fences["left"].add(position)


    side_count+= count_contiguous_fences(fences["top"],HORIZONTAL)
    side_count+= count_contiguous_fences(fences["bottom"],HORIZONTAL)
    side_count+= count_contiguous_fences(fences["right"],VERTICAL)
    side_count+= count_contiguous_fences(fences["left"],VERTICAL)

    total_price+= side_count*area
    

print(total_price)
