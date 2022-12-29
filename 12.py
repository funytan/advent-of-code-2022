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
    

mat = []
start = None
end = None
row_idx = 0

with open('inputs/input_12.txt', 'r') as f:
    while True:
        direcs = [(0,1), (-1,0), (1,0), (0,-1)]
        inp = f.readline().strip()
        if not inp:
            break
        row = []
        for col_idx, char in enumerate(inp):
            if char == 'S':
                start = [row_idx, col_idx]
                row.append(ord('a')-97)
            elif char == 'E':
                end = (row_idx, col_idx)
                row.append(ord('z')-97)
            else:
                row.append(ord(char)-97)
        row_idx += 1
        mat.append(row)
        
    
    num_r = len(mat)
    num_c = len(mat[0])
    check = True
    ls = []
    for row_idx in range(num_r):
        for col_idx in range(num_c):
            if mat[row_idx][col_idx] == 0:  
                ls.append((row_idx, col_idx))
    print()
    steps = 0
    visited = set()
    while ls and check:
        new_ls = []
        for node in ls:
            row_idx, col_idx = node
            visited.add((row_idx,col_idx))
            val = mat[row_idx][col_idx]
            for direc in direcs:
                new_row_idx, new_col_idx = row_idx + direc[0], col_idx+direc[1]
                if (new_row_idx, new_col_idx) in visited:
                    continue
                if 0<=new_row_idx<num_r and 0<=new_col_idx< num_c:
                    new_val = mat[new_row_idx][new_col_idx]
                    if new_val <= (val+1):
                        if (new_row_idx,new_col_idx) == end:
                            check=False
                            break
                        visited.add((new_row_idx,new_col_idx))
                        new_ls.append([new_row_idx, new_col_idx])
            if not check:
                break
        steps += 1
        ls = new_ls
        # print(ls)
        # if steps == 10:
        #     break
    
    print(steps)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    