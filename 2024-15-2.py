def extract_data_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    
def move_robot(pos, move):
    dy, dx = DIRS[move]
    return pos[0] + dy, pos[1] + dx


def get_pos_robot(warehouse):
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == '@':
                return y,x

def get_connected_boxes(start, warehouse, move):
    stack = [start]
    zone = {start}

    direction = [(-1,0), (-1,-1), (-1,1)] if move == '^'  else [(1,0), (1,-1), (1,1)]
    while stack:
        y, x = stack.pop() 
        for dy, dx in direction:
            n = (y + dy, x + dx)
            if warehouse[n[0]][n[1]] == "[":
                zone.add(n)
                stack.append(n)

    return zone
def can_moves_boxes(boxes, warehouse, move):
    
    direction = [(-1,0),(-1,1)] if move == '^' else [(1,0),(1,1)]

    for box in boxes:
        y,x = box
        for dy, dx in direction:
            n = (y + dy, x + dx)
            if warehouse[n[0]][n[1]] == "#":
                return False
    return True

def get_moved_boxes(boxes, move):
    direction = (-1,0) if move == '^' else (1,0)
    moved_boxes = set()
    for box in boxes:
        y,x = box
        dy, dx = direction
        moved_box = (y + dy, dx + x)
        moved_boxes.add(moved_box)
    
    return moved_boxes

DIRS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}


file = "data/2024_15_map.txt"
warehouse = extract_data_file(file)
file_move = "data/2024_15_moves.txt"
moves = extract_data_file(file_move)
moves = [list(line) for line in moves]

warehouse = [list(line) for line in warehouse]

other_warehouse = []
for i, line in enumerate(warehouse):
    other_warehouse.append([])
    for e in line:
        if e == '#':
            other_warehouse[i].append('#')
            other_warehouse[i].append('#')
        elif e == '.':
            other_warehouse[i].append('.')
            other_warehouse[i].append('.')
        elif e == 'O':
            other_warehouse[i].append('[')
            other_warehouse[i].append(']')
        elif e == '@':
            other_warehouse[i].append('@')
            other_warehouse[i].append('.')





pos_robot = get_pos_robot(other_warehouse)
other_warehouse[pos_robot[0]][pos_robot[1]] = '.'


for line in moves:
    for move in line :

        p = move_robot(pos_robot, move)
        
        if other_warehouse[p[0]][p[1]] == '.' :
            pos_robot = p
        elif other_warehouse[p[0]][p[1]] != '#':

            p_start = p

            if move in ('>', '<'):

                border_box = '[' if move == '>' else ']'
                dir = 2 if move == '>' else -2
            
                while other_warehouse[p[0]][p[1]] == border_box :
                    p = (p[0],p[1]+dir) 
            

                if other_warehouse[p[0]][p[1]] == '.':
                        other_warehouse[p[0]].pop(p[1])
                        other_warehouse[p_start[0]].insert(p_start[1] , '.')
                        pos_robot = p_start


            if move in ('v','^') :

                if other_warehouse[p[0]][p[1]] == '[':
                    
                    boxes=get_connected_boxes(p,other_warehouse,move)

                elif other_warehouse[p[0]][p[1]] == ']':

                    y,x = p
                    p_box = (y,x-1)
                    boxes=get_connected_boxes(p_box,other_warehouse,move)

                if can_moves_boxes(boxes, other_warehouse,move):
                    moved_boxes = get_moved_boxes(boxes,move)

                    for box in boxes :
                        other_warehouse[box[0]][box[1]] = '.'
                        other_warehouse[box[0]][box[1]+1] = '.'
                    
                    for moved_box in moved_boxes : 
                        other_warehouse[moved_box[0]][moved_box[1]] = '['
                        other_warehouse[moved_box[0]][moved_box[1]+1] = ']'
                        
                    pos_robot = p
        
        
     

sum_GPS_boxes = 0



for y in range(len(other_warehouse)) : 
    for x in range(len(other_warehouse[y])) :
        if other_warehouse[y][x] == '[' : 
            sum_GPS_boxes+= y*100 + x

print(sum_GPS_boxes)


