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


dic = {'direcs':{}, 'files':{}}
levels = [dic]


with open('inputs/input_8_1.txt', 'r') as f:
    mat = []
    while True:
        curr_dic = levels[-1]
        inp = f.readline().strip()
        if not inp:
            break
        row = []
        for h in inp:
            row.append(int(h))
        mat.append(row)
        
    num_r = len(mat)
    num_c = len(mat[0])
    
    def get_scenic_score(r,c):
        h = mat[r][c]
        # top
        top = 0
        for i in range(r-1, -1, -1):
            top += 1
            if mat[i][c] >= h:
                break            
        # btm
        btm = 0
        for i in range(r+1, num_r):
            btm += 1
            if mat[i][c] >= h:
                break
        # left
        left = 0
        for j in range(c-1, -1, -1):
            left += 1
            if mat[r][j] >= h:
                break
        # right
        right = 0
        for j in range(c+1, num_c):
            right += 1
            if mat[r][j] >= h:
                break
        return top*btm*left*right
    
    maxi = 0
    for c in range(1, num_c-1): # no need to consider the edges
        for r in range(1, num_r-1):
            maxi = max(maxi, get_scenic_score(r,c))
            
    print(maxi)