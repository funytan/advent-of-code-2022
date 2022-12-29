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

mat = [[' ' for _ in range(1000)] for _ in range(1000)]

biggest_y = 168
with open('inputs/input_14.txt', 'r') as f:
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        lines = inp.split(' -> ')
        prev_x = None
        prev_y = None
        for line in lines:
            x, y  = list(map(int, line.split(',')))
            if prev_x is not None:
                if prev_x > x:
                    s_x, b_x = x, prev_x
                elif prev_x < x:
                    s_x, b_x = prev_x, x
                else:
                    s_x, b_x = prev_x, x
                if prev_y > y:
                    s_y, b_y = y, prev_y
                elif prev_y < y:
                    s_y, b_y = prev_y, y
                else:
                    s_y, b_y = prev_y, y
                for i in range(s_x, b_x+1):
                    for j in range(s_y, b_y+1):
                        mat[j][i] = '#'
            # biggest_y = max(y, biggest_y)
    
            prev_x = x
            prev_y = y
            
    for j in range(1000):
        mat[biggest_y][j] = '#'
    
    check=True
    dropped = 0
    movements = [[1,0], [1, -1], [1, 1]]
    
    while check:
        curr_r = 0
        curr_c = 500
        movement_idx = 0
        
        while movement_idx < 3:
            move = movements[movement_idx]
            new_r, new_c = curr_r+move[0], curr_c + move[1]
            if mat[new_r][new_c] == '#' or mat[new_r][new_c] == 'o':
                movement_idx += 1
            else:
                movement_idx = 0
                curr_r, curr_c = new_r, new_c
            
        if movement_idx == 3:
            mat[curr_r][curr_c] = 'o'
            if curr_r==0 and curr_c == 500:
                dropped += 1
                break
        
        dropped += 1
        
        
    # for r in range(12):
    #     print(mat[r][485:515])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    