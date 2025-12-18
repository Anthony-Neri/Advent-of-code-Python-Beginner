def extract_data_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    


file = "data/2024_5_order.txt"

puzzle_order = extract_data_file(file)

order_array = []
for line in puzzle_order:
    order_array.append([int(x) for x in line.split("|")])

file2 = "data/2024_5_maj.txt"

puzzle_maj = extract_data_file(file2)


maj_array = []
for line in puzzle_maj:
    maj_array.append([int(x) for x in line.split(",")])



sumMidNumberMajGood = 0

for y in range(len(maj_array)):
    numberGood = 0
    tryOk = 0
    while numberGood != len(maj_array[y])-1:
        numberGood = 0
        for x in range(len(maj_array[y])-1):
            numberIsGood = False

            
            for a, b in order_array: 
                if maj_array[y][x] == a and maj_array[y][x+1] == b:
                    numberIsGood = True
                    break
                elif maj_array[y][x] == b and maj_array[y][x+1] == a:
                    maj_array[y][x] = a 
                    maj_array[y][x+1] = b




            #print(maj_array[y][x],numberIsGood)
            if numberIsGood:
                numberGood+=1

        tryOk+=1

    if tryOk > 1:
        sumMidNumberMajGood+=maj_array[y][len(maj_array[y])//2]





print (sumMidNumberMajGood)
