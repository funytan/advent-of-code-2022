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
import sys
sys.setrecursionlimit(100000)


mat = {}
ls_x = []
ls_y = []
ls_z = []
direcs = [(0,1,0), (0,-1,0), (1,0,0), (-1,0,0), (0,0,-1), (0,0,1)]
ans= 0 
with open('inputs/input_18.txt', 'r') as f:
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        x,y,z = list(map(int, inp.split(',')))
        ls_x.append(x)
        ls_y.append(y)
        ls_z.append(z)
        ans += 6
        for direc in direcs:
            new_x, new_y, new_z = x+ direc[0], y + direc[1], z +  direc[2]
            if (new_x, new_y, new_z) in mat:
                ans -= 2
        mat[(x,y,z)] = True

# dfs
mini_x, maxi_x = min(ls_x), max(ls_x)
mini_y, maxi_y = min(ls_y), max(ls_y)
mini_z, maxi_z = min(ls_z), max(ls_z)

visited = set()

def dfs(node):
    x, y, z = node
    visited.add((x,y,z))
    if (x < mini_x or x > maxi_x or y < mini_y or y > maxi_y or z < mini_z or z > maxi_z):
        return True
    if (x,y,z) in mat:
        return False
    pocket.add((x,y,z))
    outside = False
    for direc in direcs:
        new_x, new_y, new_z = x+ direc[0], y + direc[1], z +  direc[2]
        if (new_x, new_y, new_z) not in visited:
            # visited.add((new_x, new_y, new_z))
            outside |= dfs((new_x, new_y, new_z))
    return outside

def get_area(node_ls):
    new_mat = {}
    new_ans = 0
    for node in node_ls:
        new_ans += 6
        x,y,z = node
        for direc in direcs:
            new_x, new_y, new_z = x+ direc[0], y + direc[1], z +  direc[2]
            if (new_x, new_y, new_z) in new_mat:
                new_ans -= 2
        new_mat[(x,y,z)] = True
    return new_ans

# ls = []

for x in range(mini_x, maxi_x+1):
    for y in range(mini_y, maxi_y+1):
        for z in range(mini_z, maxi_z+1):
            if (x,y,z) in mat or (x,y,z) in visited: 
                continue
            pocket = set()
            outside = dfs((x,y,z))
            if not outside:
                new_ans = get_area(list(pocket))
                ans -= new_ans
                # for node in pocket:
                    # ls.append(node)
                # print(new_ans, list(pocket))
print(ans)
        
            
                