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
import math
import re  
import time
import sys
sys.setrecursionlimit(100000)


mat = []

blizzards_dic = {
    '^': set(),
    '>': set(),
    '<': set(),
    'v': set(),
}

safe_grounds = set()
all_blizzards = set()

with open('inputs/input_24.txt', 'r') as f:
    row_idx = 0
    while True:
        inp = f.readline()[:-1]
        if not inp:
            break
        mat.append(inp)
        for col_idx, char in enumerate(inp):
            if char == '.':
                safe_grounds.add((row_idx, col_idx))
            elif char == '#':
                continue
            else:
                blizzards_dic[char].add((row_idx, col_idx))
                all_blizzards.add((row_idx, col_idx))
        
        row_idx += 1
    
    row_min_limit = 0
    row_max_limit = row_idx-1
    col_min_limit = 0
    col_max_limit = len(mat[0])-1
    
    num_cycles = math.lcm(row_max_limit-row_min_limit-1,col_max_limit-col_min_limit-1)

states = []
cycle_cnt = 0
blizzards_states = []

while cycle_cnt < num_cycles:
    # if cycle_cnt % 100==0:
    #     print(cycle_cnt)
    all_blizzards = set()
    safe_grounds = set([(0,1), (row_max_limit,col_max_limit-1)])
    new_blizzards_dic = {
        '^': set(),
        '>': set(),
        '<': set(),
        'v': set(),
    }
    
    for direc in blizzards_dic:
        for bliz in blizzards_dic[direc]:
            row, col = bliz
            if direc == '^':
                change = (-1, 0)
                new_row, new_col = row+change[0], col+change[1]
                if new_row == row_min_limit:
                    new_row = row_max_limit - 1
            elif direc == 'v':
                change = (1, 0)
                new_row, new_col = row+change[0], col+change[1]
                if new_row == row_max_limit:
                    new_row = row_min_limit + 1          
            elif direc == '<':
                change = (0, -1)
                new_row, new_col = row+change[0], col+change[1]
                if new_col == col_min_limit:
                    new_col = col_max_limit - 1          
            elif direc == '>':
                change = (0, 1)
                new_row, new_col = row+change[0], col+change[1]
                if new_col == col_max_limit:
                    new_col = col_min_limit + 1
            
            new_blizzards_dic[direc].add((new_row, new_col))
            all_blizzards.add((new_row, new_col))
        
    for row in range(row_min_limit+1, row_max_limit):
        for col in range(col_min_limit+1, col_max_limit):
            if (row, col) not in all_blizzards:
                safe_grounds.add((row, col))
    
    states.append(safe_grounds)
    blizzards_states.append(new_blizzards_dic)
    blizzards_dic = new_blizzards_dic
    cycle_cnt += 1

    # for row in range(row_min_limit+1, row_max_limit):
    #     print_row = ''
    #     for col in range(col_min_limit+1, col_max_limit):
    #         if (row, col) in new_nodes:
    #             print_row += 'E'
    #         else:
    #             print_row += '#'
    #     print(print_row)
    # print(minute)
    # print()

# goto goal

minute = 0
check = True
nodes = set([(0,1)])
movements = [(0,1), (1,0), (0,-1), (-1,0), (0,0)]

while check:
    # print(len(nodes))
    new_nodes = set()
    safe_grounds = states[minute%num_cycles]
    for node in nodes: 
        row, col  = node
        for movement in movements:
            new_row, new_col = row + movement[0], col + movement[1]
            if (new_row, new_col) in safe_grounds:
                new_nodes.add((new_row, new_col))
                if (new_row, new_col) == (row_max_limit,col_max_limit-1):
                    check = False
    minute += 1
    nodes = new_nodes
    
# goto start

check = True
nodes = set([(row_max_limit,col_max_limit-1)])

while check:
    # print(len(nodes))
    new_nodes = set()
    safe_grounds = states[minute%num_cycles]
    for node in nodes: 
        row, col  = node
        for movement in movements:
            new_row, new_col = row + movement[0], col + movement[1]
            if (new_row, new_col) in safe_grounds:
                new_nodes.add((new_row, new_col))
                if (new_row, new_col) == (0,1):
                    check = False
    minute += 1
    nodes = new_nodes
    
# goto goal
check = True
nodes = set([(0,1)])

while check:
    # print(len(nodes))
    new_nodes = set()
    safe_grounds = states[minute%num_cycles]
    for node in nodes: 
        row, col  = node
        for movement in movements:
            new_row, new_col = row + movement[0], col + movement[1]
            if (new_row, new_col) in safe_grounds:
                new_nodes.add((new_row, new_col))
                if (new_row, new_col) == (row_max_limit,col_max_limit-1):
                    check = False
    minute += 1
    nodes = new_nodes
print(minute)
        
                
        
    