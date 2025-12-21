import time

stones = {6571:1,0:1,5851763:1,526746:1,23:1,69822:1,9:1,989:1}


def blink(stones):
    stonesAfterBlink = {}

    for stone,nbr in stones.items():
        if stone == 0:
            stonesAfterBlink[1]=stonesAfterBlink.get(1,0)+nbr
        elif len(str(stone))%2 == 0:
            s = str(stone)
            mid = len(s) // 2
            left = int(s[:mid])
            right = int(s[mid:])
            stonesAfterBlink[left]=stonesAfterBlink.get(left,0)+nbr
            stonesAfterBlink[right]=stonesAfterBlink.get(right,0)+nbr
        else:
            stone = stone*2024
            stonesAfterBlink[stone]= stonesAfterBlink.get(stone,0) +nbr

        
    return stonesAfterBlink

start = time.perf_counter()

for i in range(75):
    stones = blink(stones)


print(sum(stones.values()))

end = time.perf_counter()
print(f"Temps d'exécution : {(end - start)*1000:.3f} ms")
