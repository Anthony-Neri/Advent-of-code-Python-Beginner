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
MID_X = int((MAX_X-1)/2)
MID_Y = int((MAX_Y-1)/2)
pos_robots =  defaultdict(int)
for p_robot, v_robot in robots : 

    p = p_robot
    v = v_robot
    for i in  range(100):
      p = robot_walk(p,v,MAX_X,MAX_Y)

    x,y = p 
    if x != MID_X and y != MID_Y:
        if x < MID_X and y < MID_Y:
            pos_robots[1]+=1
        elif x > MID_X and y < MID_Y:
            pos_robots[2]+=1
        elif x < MID_X and y > MID_Y:
            pos_robots[3]+=1
        elif x > MID_X and y > MID_Y:
            pos_robots[4]+=1

safety_factor = 1
print(pos_robots)
for quadrant in pos_robots.values():
    safety_factor*=quadrant

print(safety_factor)

end = time.perf_counter()
print(f"Temps d'exécution : {(end - start)*1000:.3f} ms")
