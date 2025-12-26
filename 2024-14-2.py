import re
import time
from collections import defaultdict
start = time.perf_counter()
def extract_data_file(file):

    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()
    

file = "data/2024_14.txt"

data = extract_data_file(file)
robots = []
for line in data:
    matches = re.findall(r"-?\d{1,3}", line)
    robots.append([(int(matches[0]),int(matches[1])),(int(matches[2]),int(matches[3])) ])


def robot_walk(p,v,max_x,max_y):
    vx, vy = v

    px, py = p

    if px + vx >= max_x:
        px = px + vx - max_x
    elif px + vx < 0 :
        px = px + vx + max_x
    else :
        px = px + vx
    
    if py + vy >= max_y:
        py = py + vy - max_y
    elif py + vy < 0 :
        py = py + vy + max_y
    else :
        py = py + vy
    
    return px, py

 
MAX_X = 101
MAX_Y = 103
find_motif = set()
grp = 0
sec = 0
for a in range(10000):
    
    pos_robots =  set()
    for i, robot in enumerate(robots) : 

        p = robot[0]
        v = robot[1]
        
        p = robot_walk(p,v,MAX_X,MAX_Y)

        robots[i][0] = p
        
        pos_robots.add(p)
    
    for pos_robot in pos_robots:
        grp_t= 0
        d = [(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1),(0,1),(0,-1)]
        for dx, dy in d:
            x,y = p 
            n = (x+dx,y+dy)
            if n in pos_robots:
                grp_t+=1

    if grp_t > grp :
        grp = grp_t
        find_motif = pos_robots.copy()
        sec = a + 1

    

    
print(sec)
for y in range(MAX_Y):
    for x in range(MAX_X):
        if (x,y) in find_motif : 
            print('.', end='')
        else:
            print(' ', end='')
    print()
    



end = time.perf_counter()
print(f"Temps d'exécution : {(end - start)*1000:.3f} ms")
