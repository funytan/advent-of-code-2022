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
import re  
import time
import sys
sys.setrecursionlimit(100000)

mat = []
num_c = 150

with open('inputs/input_22.txt', 'r') as f:
    idx = 0
    while True:
        inp = f.readline()[:-1]
        if not inp:
            break
        mat.append(inp + ' '*(num_c-len(inp)))
    
    num_r = len(mat)
    num_c = max([len(row) for row in mat])
    rows_store = [{} for _ in range(num_r)]
    cols_store = [{} for _ in range(num_c)]
    
    for i in range(num_r):
        walls = []
        start = None
        end = None
        
        for j in range(num_c):
            ele = mat[i][j]
            if ele != ' ' and start is None:
                start = j
            if ele == ' ' and start is not None and end is None:
                end = j-1
            if ele == '#':
                walls.append(j)
        if end is None:
            end = j
        
        rows_store[i]['start'] = start
        rows_store[i]['end'] = end
        rows_store[i]['walls'] = walls
        
        # first 50 rows
        if 0<=i<50:
            rows_store[i]['right_trans'] = ('row', 149-i, 'L')
            rows_store[i]['left_trans'] = ('row', 149-i, 'R')
            # row, 100-149
        if 50<=i<100:
            rows_store[i]['right_trans'] = ('col', 50+i, 'U')
            # row, 100-149
            rows_store[i]['left_trans'] = ('col', i-50, 'D')
            
        if 100<=i<150:
            rows_store[i]['right_trans'] = ('row', 149-i, 'L')
            # row, 100-149
            rows_store[i]['left_trans'] = ('row', 149-i, 'R')
        if 150<=i<200:
            rows_store[i]['right_trans'] = ('col', i-100, 'U')
            # row, 100-149
            rows_store[i]['left_trans'] = ('col', i-100, 'D')
        
            
    for j in range(num_c):
        walls = []
        start = None
        end = None
        walls_up = {} # idx: steps
        walls_down = {} # idx: steps
        for i in range(num_r):
            ele = mat[i][j]
            if ele != ' ' and start is None:
                start = i
            if ele == ' ' and start is not None and end is None:
                end = i-1
            if ele == '#':
                walls.append(i)
        if end is None:
            end = i
        
        cols_store[j]['start'] = start
        cols_store[j]['end'] = end
        cols_store[j]['walls'] = walls

        # first 50 cols
        if 0<=j<50:
            cols_store[j]['down_trans'] = ('col', 100+j, 'D')
            cols_store[j]['up_trans'] = ('row', 50+j, 'R')
            # row, 100-149
        if 50<=j<100:
            cols_store[j]['down_trans'] = ('row', 100+j, 'L')
            cols_store[j]['up_trans'] = ('row', 100+j, 'R')
        if 100<=j<150:
            cols_store[j]['down_trans'] = ('row', j-50, 'L')
            cols_store[j]['up_trans'] = ('col', j-100, 'U')
                      
    inp = f.readline().strip()
    
    idx = 0
    curr = 0
    row = 0
    col = rows_store[0]['start']
    face = 'R' 
    faces_trans_cw = {
        'R':'D',
        'D':'L',
        'L':'U',
        'U':'R',
    }
    faces_trans_acw = {
        'D':'R',
        'L':'D',
        'U':'L',
        'R':'U',
    }
    
    def execute_movement(row, col, face, steps):
        print(row, col, face, steps)
        if mat[row][col] == '#':
            return None
        if steps == 0:
            return row, col, face
        
        # transitions
        if (
                (face == 'R' and col == rows_store[row]['end']) or
                (face == 'L' and col == rows_store[row]['start']) or
                (face == 'D' and row == cols_store[col]['end']) or
                (face == 'U' and row == cols_store[col]['start'])
            ):
                
                print('here')
                if face == 'R':
                    row_or_col, num, new_face = rows_store[row]['right_trans']
                elif face == 'L':
                    row_or_col, num, new_face = rows_store[row]['left_trans']
                elif face == 'D':
                    row_or_col, num, new_face = cols_store[col]['down_trans']
                else:
                    row_or_col, num, new_face = cols_store[col]['up_trans']
                    
                    
                if row_or_col == 'row':
                    if new_face == 'R':
                        movement = execute_movement(num, rows_store[num]['start'], new_face, steps-1)
                    else: #'L'
                        movement = execute_movement(num, rows_store[num]['end'], new_face, steps-1)
                else:
                    if new_face == 'D':
                        movement = execute_movement(cols_store[num]['start'], num, new_face, steps-1)
                    else: #'U'
                        movement = execute_movement(cols_store[num]['end'], num, new_face, steps-1)
                            
        else:
            if face == 'R':
                movement = execute_movement(row, col+1, face, steps-1)
            if face == 'L':
                movement = execute_movement(row, col-1, face, steps-1)
            if face == 'D':
                movement = execute_movement(row+1, col, face, steps-1)
            if face == 'U':
                movement = execute_movement(row-1, col, face, steps-1)
        
        if movement is not None:
            return movement
        else:
            return row, col, face
    
    while idx < len(inp):
        char = inp[idx]
        if char != 'L' and char != 'R':
            curr *= 10
            curr += int(char)
        else: # excecute movement then turn
            print(curr+1, 'start movement')
            row, col, face = execute_movement(row, col, face, curr)
            curr = 0
            if char == 'R':
                face = faces_trans_cw[face]
            else:
                face = faces_trans_acw[face]
            print(row, col, face, 'end movement')
            # if idx > 10:
            #     assert 1==2
        idx += 1
    
    print(curr+1, 'start movement')
    row, col, face = execute_movement(row, col, face, curr)
    
    
    face_score = {'R':0,'D':1,'L':2,'U':3,}
    print(row, col, face)
    print(1000*(row+1) + 4*(col+1) + face_score[face])
                
        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
        
    