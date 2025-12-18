def extract_data_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    


file = "data/2024_6.txt"
puzzle = extract_data_file(file)


lab = []
for line in puzzle:
    lab.append(list(line)) 



def whereIsGarden():
    for y in range(len(lab)):
        for x in range(len(lab[y])):
            if lab[y][x] == garden:

                posGarden.insert(0,y)
                posGarden.insert(1,x)
      

def walkGarden(posGarden, garden):

    continueWalk = True 
    nbrOfLoop = 0
    while continueWalk and nbrOfLoop < 100 :
        nbrOfLoop+=1

        while garden == '^':
            if posGarden[0]-1 < 0 :
                continueWalk = False
                break
            elif lab[posGarden[0]-1][posGarden[1]] == '#':
                garden = '>'
            else :
                lab[posGarden[0]-1][posGarden[1]] = 'X'
                posGarden[0]-=1
        
        while garden == '>':
            if posGarden[1]+1 >= len(lab[posGarden[0]]) :
                continueWalk = False
                break
            elif lab[posGarden[0]][posGarden[1]+1] == '#':
                garden = 'v'
            else :
                lab[posGarden[0]][posGarden[1]+1] = 'X'
                posGarden[1]+=1

        while garden == 'v':
            if posGarden[0]+1 >= len(lab) :
                continueWalk = False
                break
            elif lab[posGarden[0]+1][posGarden[1]] == '#':
                garden = '<'
            else :
                lab[posGarden[0]+1][posGarden[1]] = 'X'
                posGarden[0]+=1
        
        while garden == '<':
            if posGarden[1]-1 < 0 :
                continueWalk = False
                break
            elif lab[posGarden[0]][posGarden[1]-1] == '#':
                garden = '^'
            else :
                lab[posGarden[0]][posGarden[1]-1] = 'X'
                posGarden[1]-=1
    
    return nbrOfLoop
            




                
posGarden = []
garden = '^'



whereIsGarden()

lab[posGarden[0]][posGarden[1]]= 'X'
loop = 0

for y in range(len(lab)):
    for x in range(len(lab[y])):

        if lab[y][x] == "#":
            continue

        
        lab[y][x] = '#'

        nbrOfLoop = walkGarden(posGarden.copy(), garden)

        if nbrOfLoop >= 100:
            loop += 1

        
        lab[y][x] = '.'


print (loop)
