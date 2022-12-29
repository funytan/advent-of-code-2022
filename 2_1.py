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


            
with open('inputs/input_2_1.txt', 'r') as f:
    outcome = {
        'A': {'X':3, 'Y':6, 'Z':0}, 
        'B': {'X':0, 'Y':3, 'Z':6}, 
        'C': {'X':6, 'Y':0, 'Z':3}, 
    }
    play_score = {'X': 1, 'Y': 2, 'Z': 3} 
    
    score = 0
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        opp, me = inp.split()
        score += outcome[opp][me]
        score += play_score[me]
    print(score)