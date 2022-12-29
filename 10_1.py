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
        

# signal_strengths = [20, 60,100,140,180,220]
X = 1
itr = 0
# strength = 0
dq = deque()
mat = [['.' for _ in range(40)]for _ in range(6)]


with open('inputs/input_10_1.txt', 'r') as f:
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        inp_split = inp.split()
        dq.append(None)
        if len(inp_split) == 2:
            op, num = inp.split()
            num = int(num)
            dq.append(num)
        
        
    while dq:
        sprite_pos = (X-1,X,X+1)
        if (itr%40) in sprite_pos:
            mat[itr//40][itr%40] ='#'
        item = dq.popleft()
        if item is not None:
            X += item
        itr += 1
        # print(X, itr)
    for row in mat:
        print(' '. join(row))