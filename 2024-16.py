import heapq


def solve_part1(filename):
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f]

    
    DIRECTIONS = [(0,1),(-1,0),(0,-1),(1,0)]
    # (y , x , d) = score
    distances = {}

    pq = []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (y,x)
            if cell == 'E':
                end = (y,x)

    start_state = (start[0], start[1] , 0)
    distances[start_state] = 0

    heapq.heappush(pq, (0, *start_state))

    while pq :

        score, y, x, d = heapq.heappop(pq)

        if distances.get((y, x, d), float("inf")) < score:
            continue
        
        if (y, x) == end:

            
            print(distances)
            return score
        

        #Avancer tout droit

        dy, dx = DIRECTIONS[d]

        ny = y + dy
        nx = x + dx



        if grid[ny][nx] != '#' : 

            new_score = score + 1
            next_state = (ny, nx ,d)
            old_score = distances.get(next_state, float("inf")) # SI la clé next_state n'existe pas, valeur retournée infinie
            
            if new_score < old_score : 
                distances[next_state] = new_score
                heapq.heappush(pq,(new_score, *next_state))

        #Tourner
        for turn in (1, -1):
            nd = d + turn
            if nd == 4 :
                nd = 0
            if nd == -1:
                nd = 3
        
            new_score = score + 1000
            next_state = (y, x, nd)
            old_score = distances.get(next_state, float("inf"))

            if new_score < old_score : 
                distances[next_state] = new_score
                heapq.heappush(pq,(new_score, *next_state ))


        

file = "data/2024_16.txt"

print(solve_part1(file))







    
    
