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


            
with open('inputs/input_4_1.txt', 'r') as f:
    overlaps = 0
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        seg_1, seg_2 = inp.split(',')
        s1, e1 = list(map(int, seg_1.split('-')))
        s2, e2 = list(map(int, seg_2.split('-')))
        if (s1 <= s2 and e1 >= e2) or(s1 >= s2 and e1 <= e2):
            overlaps += 1

    print(overlaps)
    