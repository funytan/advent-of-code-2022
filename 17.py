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
import time

state = {}
left_bound = 0
right_bound = 8
highest = 0

# initilaize floor
for j in range(left_bound+1, right_bound):
    state[(highest, j)] = True
    
# initialize shapes
shapes = [
    [(4,3), (4,4), (4,5), (4,6)],
    [(4,4), (5,3), (5,4), (5,5), (6,4)],
    [(4,3), (4,4), (4,5), (5,5), (6,5)],
    [(4,3), (5,3), (6,3), (7,3)],
    [(4,3), (5,3), (4,4), (5,4)],    
]


# @lru_cache(maxsize=None)
def simulate(tiles, direc):
    # print(direc)
    # print(tiles, direc)
    if direc == 'd':
        change = (-1, 0)
    elif direc == 'l':
        change = (0, -1)
    elif direc == 'r':
        change = (0, 1)
    
    check = True
    new_tiles = []
    for tile in tiles:
        i, j = tile
        new_i, new_j = i + change[0], j + change[1]
        new_tiles.append((new_i, new_j))
        if (new_i, new_j) in state or (not (left_bound<new_j<right_bound)):
            check = False
            
    if check: # return updated tiles
        return new_tiles
    else:
        if direc == 'd':
            return None
        else:
            return tiles

with open('inputs/input_17.txt', 'r') as f:
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        directions = inp

d_idx = 0
shape_idx = 0

while shape_idx <100000:
    shape = shapes[shape_idx%5]
    curr_parity = 0
    cont = True
    tiles = [(tile[0] + highest, tile[1]) for tile in shape]
    while cont:
        if (curr_parity % 2)==0:
            if directions[d_idx%len(directions)] == '<':
                new_tiles = simulate(tiles, 'l')
            else:
                new_tiles = simulate(tiles, 'r')
            d_idx += 1
        else:
            new_tiles = simulate(tiles, 'd')
        if new_tiles is None:
            cont = False
            for tile in tiles:
                highest = max(highest, tile[0])
                state[tile] = True
        else:
            tiles = new_tiles
        
        if d_idx % 10091 == 5 and (curr_parity % 2)==1:
            for i in range(highest+8,highest - 10,-1):
                row = []
                for j in range(1,8):
                    if (i,j) in state or (i,j) in tiles:
                        row.append('*')
                    else:
                        row.append('.')
                print(''.join(row))
            print(shape_idx, highest, new_tiles)
            time.sleep(2)
        if d_idx % 10091 == 750 and (curr_parity % 2)==1:
            for i in range(highest+8,highest - 10,-1):
                row = []
                for j in range(1,8):
                    if (i,j) in state or (i,j) in tiles:
                        row.append('*')
                    else:
                        row.append('.')
                print(''.join(row))
            print(shape_idx, highest, new_tiles)
            time.sleep(2)
        curr_parity += 1
    shape_idx += 1
    # break
print(highest)
print(shape_idx%5)
for i in range(highest,highest-10, -1):
    row = []
    for j in range(1,8):
        if (i,j) in state or (i,j) in tiles:
            row.append('*')
        else:
            row.append('.')
    print(''.join(row))

            
    
    
#    2659 height, 1730 shapes

# (1000000000000-10)//1730 = 578034682
#  1536994219438 + 2694 - 2659 = 1536994219473
    
# 1536994219438

# 1740 2694
# 3470 5353
# 5200 8012