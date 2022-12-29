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

def move(direc, knots):
    
    for i in range(9):
        head = knots[i]
        tail = knots[i+1]
        # UP
        if direc == 'U':
            if i == 0:
                head = (head[0] - 1, head[1])
        # DOWN
        if direc == 'D':
            if i == 0:
                head = (head[0] + 1, head[1])
        # RIGHT
        if direc == 'R':
            if i == 0:
                head = (head[0], head[1] + 1)
        # LEFT
        if direc == 'L':
            if i == 0:
                head = (head[0], head[1] - 1)
        if max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) == 2:
            diff_r = head[0] - tail[0]
            diff_r = min(1, diff_r)
            diff_r = max(-1,diff_r)
            tail = (tail[0]+ diff_r, tail[1])
            diff_c = head[1] - tail[1]
            diff_c = min(1, diff_c)
            diff_c = max(-1, diff_c)
            tail = (tail[0], tail[1] + diff_c)
        
        knots[i], knots[i+1] = head, tail
        assert(max(abs(head[0] - tail[0]), abs(head[1] - tail[1])) < 2)
    
    return knots
        

with open('inputs/input_9_1.txt', 'r') as f:
    knots = [(0,0) for _ in range(10)]
    visited = set([(0,0)])
    while True:
        inp = f.readline().strip()
        if not inp:
            break

        direc, dist = inp.split()
        dist = int(dist)
        for _ in range(dist):
            knots = move(direc, knots)
            visited.add(knots[9])
