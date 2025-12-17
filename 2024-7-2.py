def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2024_7"

data = extract_data_file(file)

data = [line.split(":") for line in data ]

for line in data:
    line[0] = int(line[0])                             
    line[1] = list(map(int, line[1].strip().split(" ")))  

# strip() pour enlever l’espace avant les nombres
# split(" ") pour séparer
# map(int, ...) pour convertir en int



def can_match_goal(goal, result, values):
    # Si la liste des valeurs est vide, vérifier si on a atteint l'objectif
    if not values:
        return goal == result
    

    if result > goal:
       return False
    
    # Récursion en ajoutant le premier élément de values
    add_result = can_match_goal(goal, result + values[0], values[1:])

    conc_result = can_match_goal(goal,int("".join(map(str, [result, values[0]]))), values[1:])
    
    if (result == 0):
       result=1
    # Récursion en multipliant le premier élément de values
    mul_result = can_match_goal(goal, result * values[0], values[1:])
    
    # Retourner true si l'une des trois récursions retourne true
    return add_result or mul_result or conc_result

sumExo1=0
for line in data:
    if can_match_goal(line[0],0,line[1]):
        sumExo1+=line[0]

print(sumExo1)
