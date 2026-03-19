def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().split(",")

file = "data/2025_2.txt"

data = extract_data_file(file)



sumBadId = 0

for line in data:
    numbers = line.split("-")


    numberOne = int(numbers[0])
    numberTwo = int(numbers[1])

    

    for i in range(numberTwo - numberOne +1):
        number = numberOne + i
        strNumber = str(number)
        midStr = int(len(strNumber)/2)
        if strNumber[:midStr] == strNumber[midStr:]:
            sumBadId+=number

print(sumBadId)
