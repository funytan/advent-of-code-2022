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


            
with open('inputs/input_3_1.txt', 'r') as f:
    priorities = 0
    cnter = 1
    overlaps = None
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        if overlaps:
            overlaps = set(inp).intersection(overlaps)
        else:
            overlaps = set(inp)
        if cnter == 3:
            badge = list(overlaps)[0]
            if 'a'<=badge<='z':
                priorities += ord(badge) - 96
            else:
                priorities += ord(badge) - 38
            cnter = 0
            overlaps = None
        cnter+=1
    print(priorities)
    