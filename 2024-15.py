def extract_data_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    


file = "data/2024_15_map.txt"
warehouse = extract_data_file(file)
file_move = "data/2024_15_moves.txt"
moves = extract_data_file(file_move)
moves = [list(line) for line in moves]

warehouse = [list(line) for line in warehouse]


def move_robot(position, move):
    y,x = position
    match move :
        case "<" :
            return (y,x-1)
        case ">" :
            return (y,x+1)
        case "^" :
            return (y-1,x)
        case "v" :
            return (y+1,x)
    
    return position

def get_pos_robot(warehouse):
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == '@':
                return (y,x)
                

pos_robot = get_pos_robot(warehouse)
warehouse[pos_robot[0]][pos_robot[1]] = '.'

for line in moves:
    for move in line :

        p = move_robot(pos_robot, move)
        

        p_start = p
        count_boxe = 0


        
        while warehouse[p[0]][p[1]] == 'O':
            count_boxe+=1
            p = move_robot(p, move) 
            

        if warehouse[p[0]][p[1]] == '.':
            if count_boxe == 0 :
                pos_robot = p
            else : 
                warehouse[p[0]][p[1]] = 'O'
                warehouse[p_start[0]][p_start[1]] = '.'
                pos_robot = p_start

sum_GPS_boxes = 0

for y in range(len(warehouse)) : 
    for x in range(len(warehouse[y])) :
        if warehouse[y][x] == 'O' : 
            sum_GPS_boxes+= y*100 + x

print(sum_GPS_boxes)


