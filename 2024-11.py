import time
stones = [6571,0,5851763,526746,23,69822,9,989]

def blink(stones):

    stonesAfterBlink = []

    for stone in stones:
        if stone == 0:
            stonesAfterBlink.append(1)
        elif len(str(stone))%2 == 0:
            
            s = str(stone)
            mid = len(s) // 2

            left = int(s[:mid])
            right = int(s[mid:])
            stonesAfterBlink.append(left)
            stonesAfterBlink.append(right)
        else :
            stonesAfterBlink.append(stone*2024)
    
    return stonesAfterBlink

start = time.perf_counter()

for i in range(25):
    stones = blink(stones)

print(len(stones))

end = time.perf_counter()
print(f"Temps d'exécution : {(end - start)*1000:.3f} ms")

# Méthode très simple mais très peu efficace quand le nombre de pierres dans le tableau devient important.
