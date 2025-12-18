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
    

# Récupération de la position des fichiers, de leur ID et de leur taille.

files =[]

i = 0
while i < len(newData):
    if newData[i] != '.':
        fid = newData[i]
        start = i
        while i < len(newData) and fid == newData[i]:
            i+=1
        files.append([fid,start,i-start])
    else :
        i+=1

#Déplacement des fichiers par blocs 

for file in reversed(files):
    i = 0
    while  i < file[1]: # Boucle pour parcourir le tableau sans aller plus loin que la position du fichier.

        while j < file[1] and newData[j] == '.': # Parcours d'un bloc vide pour en déterminer la taille.
            j+=1
        if j-i >= file[2]: # Si la taille du bloc vide est supérieure ou égale à la taille du bloc du fichier.
            for k in range(file[2]):
                newData[i+k] = file[0] # i est la position de départ du bloc vide.
                newData[file[1]+k] = '.' 
            break
        i+=1 # Si le bloc n'est pas un espace vide, on passe au prochain.
        


        
checkSum = 0
for i, value in enumerate(newData):
    if value != '.':
        checkSum+=i*value


print(checkSum)
