def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().split(",")

file = "data/2025_2_2.txt"

data = extract_data_file(file)



sumBadId = 0

for line in data:
    numbers = line.split("-")


    numberOne = int(numbers[0])
    numberTwo = int(numbers[1])

    

    for i in range(numberTwo - numberOne +1):
        number = numberOne + i
        strNumber = str(number)

        for y in range(len(strNumber)):

            if y != 0 :
                if len(strNumber) % y == 0:

                    parts = set( [strNumber[i:i+y] for i in range (0, len(strNumber), y)])

                    if len(parts) == 1 :

                        sumBadId+=number
                        break

print(sumBadId)

# Version longue de la ligne 32 :
# parts = []
#
# for i in range(0, len(strNumber), 2):
#     part = strNumber[i:i+2]
#     parts.append(part)
