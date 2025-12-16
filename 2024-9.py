def extract_data_file(file):

    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2024_9"


data = extract_data_file(file)

#Transformation de data en tableau de chiffres.
data = [int(x) for x in list(data[0])]

#Première phase de l'exercice.
newData = []
nb = 0
for i in range(len(data)):

    if i%2 == 0:
        for n in range(data[i]):
            newData.append(nb)
        nb+=1
    else:
        for n in  range(data[i]):
            newData.append('.')
    
# Remplissage des espaces.
for i, value in enumerate(newData):
    if value == ".":
        
        while (newData[-1] == '.' ):
            newData.pop()
                 
        
        newData[i] = newData[-1]
        newData.pop()

#Calcul du checksum
checkSum = 0
for i, value in enumerate(newData):
    checkSum+=i*value

print(checkSum)
