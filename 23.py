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

movement_deque = deque([
    [(-1,-1), (-1,0), (-1,1), (-1,0)], # N
    [(1,-1), (1,0), (1,1), (1,0)], # S
    [(-1,-1), (0,-1), (1,-1), (0,-1)], # W
    [(-1,1), (0,1), (1,1), (0,1)], # E
])

all_directions = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
    (1, 0),
    (0, 1),
    (0, -1),
    (-1, 0),
]

elves = []

with open('inputs/input_23.txt', 'r') as f:
    row_idx = 0
    while True:
        inp = f.readline()[:-1]
        if not inp:
            break
        for col_idx, char in enumerate(inp):
            if char == '#':
                elves.append((row_idx, col_idx))
        
        row_idx +=1

                    
elves_set = set(elves)
new_elves_dic = defaultdict(int)
new_elves = []    
rounds = 0
something_move = True

while something_move:
    for elf in elves:
        row, col = elf
        can_move = False
        # print(elves_set)
        for direc in all_directions:
            new_row, new_col = row + direc[0], col + direc[1]
            if (new_row,new_col) in elves_set:
                can_move = True
                break
            
        if can_move:
            for move in movement_deque:
                check = True
                for check_sq in move[:3]:
                    new_row, new_col = row + check_sq[0], col + check_sq[1]
                    if (new_row,new_col) in elves_set:
                        check = False
                        break
                if check:
                    new_elves_dic[(row + move[3][0], col + move[3][1])] += 1
                    new_elves.append((row + move[3][0], col + move[3][1], row, col))
                    break
            if not check:
                new_elves.append((row, col, row, col))
        else:
            new_elves.append((row, col, row, col))
            
    elves = []                
    something_move = False
    for new_elf in new_elves:
        new_row, new_col, old_row, old_col = new_elf
        if new_elves_dic[(new_row,new_col)] == 1:
            elves.append((new_row, new_col))
            something_move = True
        else:
            elves.append((old_row, old_col))
            
                
    rounds += 1
    new_elves = []
    new_elves_dic = defaultdict(int)
    elves_set = set(elves)
    movement_deque.append(movement_deque.popleft())
    
    # mini_row = min([elf[0] for elf in elves])
    # maxi_row = max([elf[0] for elf in elves])
    # mini_col = min([elf[1] for elf in elves])
    # maxi_col = max([elf[1] for elf in elves])
    # for i in range(mini_row, maxi_row+1):
    #     print_row = ''
    #     for j in range(mini_col, maxi_col+1):
    #         if (i,j) in elves_set:
    #             print_row += '#'
    #         else:
    #             print_row += '.'
    #     print(print_row)
    # print()
    

# mini_row = min([elf[0] for elf in elves])
# maxi_row = max([elf[0] for elf in elves])
# mini_col = min([elf[1] for elf in elves])
# maxi_col = max([elf[1] for elf in elves])

# print((maxi_row - mini_row+1) * (maxi_col - mini_col+1)- len(elves))
print(rounds)
                    
                
        
    