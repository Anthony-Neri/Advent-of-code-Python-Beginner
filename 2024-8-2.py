def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2024_8"

data_test = extract_data_file(file)

data_array = []
for line in data_test:
    data_array.append(list(line))


max_y = len(data_array)
max_x = len(data_array[0])

# Regroupement des positions des antennes via le lettre.
positions={}

for y in range(len(data_array)):
    for x in range(len(data_array[y])):
        char = data_array[y][x]
        if char != '.':
            if char not in positions:
                positions[char] = []
            positions[char].append((y, x))


#Création des deux antinodes par groupe d'antennes.
antinodes = []

for char, coords in positions.items():
    for i, c1 in enumerate(coords):
        for c2 in coords[i+1:]:
            antinode1Y = 2*c1[0]-c2[0]
            antinode1X = 2*c1[1]-c2[1]
            antinode2Y = 2*c2[0]-c1[0]
            antinode2X = 2*c2[1]-c1[1]
            
            
            while (antinode1X >=0 and antinode1Y >= 0 and antinode1X < max_x and antinode1Y < max_y):
                if (antinode1Y, antinode1X) not in antinodes:
                    antinodes.append((antinode1Y, antinode1X))
                

                antinode1Y+=c1[0]-c2[0]
                antinode1X+=c1[1]-c2[1]
                
    
            
            while (antinode2X >=0 and antinode2Y >= 0 and antinode2X < max_x and antinode2Y < max_y):
                if (antinode2Y, antinode2X) not in antinodes:
                    antinodes.append((antinode2Y, antinode2X))
                
                antinode2Y+=c2[0]-c1[0]
                antinode2X+=c2[1]-c1[1]
                
            

# Récupération de toutes les positions des antennes.

all_antennas = {c for coords in positions.values() for c in coords}

# Version longue : 
# all_antennas = set()

# for coords in positions.values():      
#     for c in coords:                   
#         all_antennas.add(c)

#Suppression des antinodes 
antinodes = [a for a in antinodes if a not in all_antennas]
# Version longue : 
# nouvelle_liste = []

# for a in antinodes:
#     if a not in all_antennas:
#         nouvelle_liste.append(a)

# antinodes = nouvelle_liste


print(len(antinodes)+len(all_antennas)) #Résultat Ok mais ne prends pas en compte s'il y a des antennes seules.


