import io, os, sys
from sys import stdin, stdout
 
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# def input(): return stdin.readline().strip()
# def read_int_list(): return list(map(int, input().split()))
# def read_int_tuple(): return tuple(map(int, input().split()))
# def read_int(): return int(input())
 
from itertools import permutations, chain, combinations, product
from math import factorial, gcd
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop, heapify
from bisect import bisect_left
from functools import lru_cache      
import re  

# mat = [[' ' for _ in range(1000)] for _ in range(1000)]

sensors = []
beacon_pos = set()
sensor_pos = set()

# mini_x = -5000000
# maxi_x = 5000000

mini_x = float('inf')
maxi_x= float('-inf')

def find_dist(pos_x, pos_y, sen_x, sen_y):
    return abs(pos_x - sen_x) + abs(pos_y - sen_y)

def construct(sen_x, sen_y, closest_dist):
    dist = closest_dist + 1
    for i in range(dist, -1, -1):
        j = dist - i
        if 0<=(sen_x+i)<=4000000 and 0<=(sen_y+j)<=4000000:
            coord_to_check[(sen_x+i,sen_y+j)]+=1
        if 0<=(sen_x-i)<=4000000 and 0<=(sen_y-j)<=4000000:
            coord_to_check[(sen_x-i,sen_y-j)]+=1
        if 0<=(sen_x+i)<=4000000 and 0<=(sen_y-j)<=4000000:
            coord_to_check[(sen_x+i,sen_y-j)]+=1
        if 0<=(sen_x-i)<=4000000 and 0<=(sen_y+j)<=4000000:
            coord_to_check[(sen_x-i,sen_y+j)]+=1

coord_to_check = defaultdict(int)

final_set = set()

with open('inputs/input_15.txt', 'r') as f:
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        vals = re.findall('-?\d+', inp)
        vals = list(map(int, vals))
        sensor = (vals[0], vals[1])
        beacon = (vals[2], vals[3])
        closest_dist = abs(vals[0] - vals[2]) + abs(vals[1] - vals[3])
        sensors.append([sensor, closest_dist,beacon])
        beacon_pos.add(beacon)
        sensor_pos.add(sensor)
        
        mini_x = min(vals[0] - closest_dist, mini_x)
        maxi_x = max(vals[0] + closest_dist, maxi_x)
        construct(vals[0], vals[1], closest_dist)

    for item in coord_to_check:
        x, y = item
        if coord_to_check[item] >=2:
            final_set.add(item)
    
    ans = 0
    print(len(final_set))
    for coord in final_set:
        check = False
        pos_x, pos_y = coord
        if (pos_x, pos_y) in beacon_pos or (pos_x, pos_y) in sensor_pos:
            check = True
        else:
            for sensor in sensors:

                dist = sensor[1]
                sen_x, sen_y = sensor[0]
                if find_dist(pos_x, pos_y, sen_x, sen_y) <= dist:
                    if pos_x == 1 and pos_y == 15: 
                        print('here')
                    check=True
                    # print(pos_x)
                    break
                # if x==-2:
                    # print(find_dist(pos_x, pos_y, sen_x, sen_y), dist, sensor[0], pos_x, pos_y)
            if not check:
                print(pos_x*4000000+pos_y)
                break
    
                
            


        
        
    # for r in range(12):
    #     print(mat[r][485:515])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    