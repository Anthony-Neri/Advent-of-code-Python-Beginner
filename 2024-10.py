def extract_data_file(file):

    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2024_10.txt"


mapExo = extract_data_file(file)

mapExo = [[int(x) for x in line.strip()] for line in mapExo]

def canWalk (pos,peak):

    value = mapExo[pos[0]][pos[1]]

    if value == 9:
        if pos not in peak:
            peak.append(pos)
        return
    
    # Vers la droite.
    if pos[1]+1 < len(mapExo[pos[0]]) and mapExo[pos[0]][pos[1]+1] == value+1:
        canWalk([pos[0],pos[1]+1],peak)
        
            
            

    # Vers la gauche.
    if pos[1]-1 >=0 and mapExo[pos[0]][pos[1]-1] == value +1:
        canWalk([pos[0],pos[1]-1],peak)
        
            
 
    
    # Vers la bas.
    if pos[0]+1 < len(mapExo) and mapExo[pos[0]+1][pos[1]] == value +1:
        canWalk([pos[0]+1,pos[1]],peak)
        
            
 
    
    # Vers la haut.
    if pos[0]-1 >=0 and mapExo[pos[0]-1][pos[1]] == value +1:
        canWalk([pos[0]-1,pos[1]],peak)
    
        

total = 0
for y in range(len(mapExo)) :
    for x in range(len(mapExo[y])):
        if mapExo[y][x] == 0 :
            peak = []
            canWalk([y,x],peak)
            total+=len(peak)

print(total)




