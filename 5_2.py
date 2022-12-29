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

crates = {i:[] for i in range(1,10)}


with open('inputs/input_5_1.txt', 'r') as f:
    while True:
        inp = f.readline()
        if not inp or inp == '\n':
            break
        for i in range(1,36,4):
            if inp[i]!=' ':
                crates[i//4+1].append(inp[i])
    for crate in crates:
        crates[crate].pop()
    
    while True:
        inp = f.readline()
        if not inp or inp == '\n':
            break
        inp = inp.replace('move', '')
        inp = inp.replace('from', '')
        inp = inp.replace('to', '')
        
        num, from_c, to_c = [int(item.strip()) for item in inp.split()]
        
        
        crates[to_c] = crates[from_c][:num] + crates[to_c]
        crates[from_c] = crates[from_c][num:]
        
        
        
        
        
        
        # seg_1, seg_2 = inp.split(',')
        # s1, e1 = list(map(int, seg_1.split('-')))
        # s2, e2 = list(map(int, seg_2.split('-')))
