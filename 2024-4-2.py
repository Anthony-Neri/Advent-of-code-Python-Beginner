def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2025_4.txt"

data = extract_data_file(file)

roll_positions =  set()

for y in range(len(data)) :
    for x in range(len(data[y])) :
        if data[y][x] == '@' :
            roll_positions.add((y,x))

def get_accessible_rolls (roll_positions) :

    accessible_rolls = set()


    adjacent_positions = {(0, 1), (0, -1), (1, 1), (1, -1), (1, 0), (-1, -1), (-1, 0), (-1, 1)}

    for roll_position in roll_positions :
        adjacent_rolls = 0
        for adjacent_position in adjacent_positions :
            y,x = roll_position
            dy,dx = adjacent_position

            adjacent_roll_position = (y + dy, x + dx)


            if adjacent_roll_position in roll_positions :
                adjacent_rolls+=1

        if adjacent_rolls < 4 :
            accessible_rolls.add(roll_position)
    return accessible_rolls

count_accessible_rolls = 0

while(len(get_accessible_rolls(roll_positions)) > 0 ) :
    count_accessible_rolls+= len(get_accessible_rolls(roll_positions))

    roll_positions-=get_accessible_rolls(roll_positions)


print(count_accessible_rolls)
