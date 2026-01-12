def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2025_1.txt"

jeu_de_donne = extract_data_file(file)

position = 50
nbrPosition0 = 0
for line in jeu_de_donne :
    number = int(line[1:])
    if line[0] == 'L':
        position-= number
    elif line[0] == 'R':
        position+= number
    
    while position > 99 :
        nbrPosition0+=1
        position-=100
    while position < 0 :
        nbrPosition0+=1
        position+=100

    
print(nbrPosition0)
