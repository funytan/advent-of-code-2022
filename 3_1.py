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

    while True:
        inp = f.readline().strip()
        if not inp:
            break
        one_error = list(set(inp[:len(inp)//2]).intersection(set(inp[len(inp)//2:])))[0]
        if 'a'<=one_error<='z':
            priorities += ord(one_error) - 96
        else:
            priorities += ord(one_error) - 38
    print(priorities)
    