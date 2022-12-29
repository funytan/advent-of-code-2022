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

ls = []
zeroth_idx = None

with open('inputs/input_20.txt', 'r') as f:
    idx = 0
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        ls.append((int(inp)*811589153, idx))
        if int(inp) == 0:
            zeroth_idx = idx
        idx += 1
        
ls_move = ls.copy()
# print([item[0] for item in ls_move])
for _ in range(10):
    for num, idx in ls:
        # print(num, idx)
        found_idx = ls_move.index((num, idx))
        new_idx = (found_idx +  num) % (len(ls)-1)
        if found_idx < new_idx:
            ls_move = ls_move[:found_idx] + ls_move[found_idx+1:new_idx+1] + [ls_move[found_idx]] + ls_move[new_idx+1:]
        elif found_idx > new_idx:
            ls_move = ls_move[:new_idx] + [ls_move[found_idx]] + ls_move[new_idx:found_idx] + ls_move[found_idx+1:]
        # print([item[0] for item in ls_move])
        # print(found_idx, new_idx)

ans = 0
found_idx = ls_move.index((0, zeroth_idx))
first, second, third = ls_move[(found_idx+1000)%len(ls)][0], ls_move[(found_idx+2000)%len(ls)][0], ls_move[(found_idx+3000)%len(ls)][0]
# print(first, second, third)
ans = first+ second +third