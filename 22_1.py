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
        walls_left = {} # idx: steps
        walls_right = {} # idx: steps
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
        if len(walls) > 0:
            row = mat[i]
            # go left to populate right
            wall_start_idx = walls[-1]
            steps = None
            wall_idx = wall_start_idx
            for j in range(wall_start_idx, start-1, -1):
                # print(j, steps, row[j])
                if row[j] == '#':
                    steps = 0
                    wall_idx = j
                else:
                    walls_right[j] = (steps, wall_idx)
                steps += 1
            # print(walls_right[147])
            # assert 1==2
            for j in range(end, wall_start_idx, -1):
                walls_right[j] = (steps, wall_idx)
                steps += 1
            # go right to populate left
            wall_start_idx = walls[0]
            steps = None
            wall_idx = wall_start_idx
            for j in range(wall_start_idx, end+1, 1):
                if row[j] == '#':
                    steps = 0
                    wall_idx = j
                else:
                    walls_left[j] = (steps, wall_idx)
                steps += 1
            for j in range(start, wall_start_idx, 1):
                walls_left[j] = (steps, wall_idx)
                steps += 1
        
        rows_store[i]['start'] = start
        rows_store[i]['end'] = end
        rows_store[i]['walls_left'] = walls_left
        rows_store[i]['walls_right'] = walls_right
        rows_store[i]['walls'] = walls

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
        if len(walls) > 0:
            # go up to populate down
            wall_start_idx = walls[-1]
            steps = None
            wall_idx = wall_start_idx
            for i in range(wall_start_idx, start-1, -1):
                # print(j, steps, row[j])
                if mat[i][j] == '#':
                    steps = 0
                    wall_idx = i
                else:
                    walls_down[i] = (steps, wall_idx)
                steps += 1
            # print(walls_right[147])
            # assert 1==2
            for i in range(end, wall_start_idx, -1):
                walls_down[i] = (steps, wall_idx)
                steps += 1
            # go right to populate left
            wall_start_idx = walls[0]
            steps = None
            wall_idx = wall_start_idx
            for i in range(wall_start_idx, end+1, 1):
                if mat[i][j] == '#':
                    steps = 0
                    wall_idx = i
                else:
                    walls_up[i] = (steps, wall_idx)
                steps += 1
            for i in range(start, wall_start_idx, 1):
                walls_up[i] = (steps, wall_idx)
                steps += 1
        
        cols_store[j]['start'] = start
        cols_store[j]['end'] = end
        cols_store[j]['walls_down'] = walls_down
        cols_store[j]['walls_up'] = walls_up
        cols_store[j]['walls'] = walls
                    
                    
    inp = f.readline().strip()
    
    idx = 0
    curr = 0
    row = 0
    col = rows_store[0]['start']
    face_idx = 0
    faces = ['R', 'D', 'L', 'U']
    
    def execute_movement(row, col, face, steps):
        if face in ('R', 'L'):
            length = rows_store[row]['end'] - rows_store[row]['start'] + 1
            # print(length)
            if face == 'R':
                if rows_store[row]['walls_right']:
                    steps_to_wall, wall_idx = rows_store[row]['walls_right'][col]
                    # print(steps_to_wall, wall_idx)
                    if steps >= steps_to_wall:
                        new_col = wall_idx-1
                    else:
                        new_col = col + steps
                else:
                    new_col = col + steps
        
            if face == 'L':
                if rows_store[row]['walls_left']:
                    steps_to_wall, wall_idx = rows_store[row]['walls_left'][col]
                    if steps >= steps_to_wall:
                        new_col = wall_idx+1
                    else:
                        new_col = col - steps
                else:
                    new_col = col - steps
            new_col = (new_col - rows_store[row]['start']) % length + rows_store[row]['start']
            return row, new_col
        if face in ('U', 'D'):
            length = cols_store[col]['end'] - cols_store[col]['start'] + 1
            if face == 'D':
                if cols_store[col]['walls_down']:
                    steps_to_wall, wall_idx = cols_store[col]['walls_down'][row]
                    if steps >= steps_to_wall:
                        new_row = wall_idx-1
                    else:
                        new_row = row + steps
                else:
                    new_row = row + steps
        
            if face == 'U':
                if cols_store[col]['walls_up']:
                    steps_to_wall, wall_idx = cols_store[col]['walls_up'][row]
                    if steps >= steps_to_wall:
                        new_row = wall_idx+1
                    else:
                        new_row = row - steps
                else:
                    new_row = row - steps
            new_row = (new_row - cols_store[col]['start']) % length + cols_store[col]['start']
            return new_row, col
    
    while idx < len(inp):
        char = inp[idx]
        if char != 'L' and char != 'R':
            curr *= 10
            curr += int(char)
        else: # excecute movement then turn
            print(row, col, faces[face_idx], curr)
            row, col = execute_movement(row, col, faces[face_idx], curr)
            curr = 0
            if char == 'R':
                face_idx += 1
            else:
                face_idx -= 1
            face_idx = face_idx % 4
        idx += 1
    print(row, col, faces[face_idx], curr)
    row, col = execute_movement(row, col, faces[face_idx], curr)
            
    print(1000*(row+1) + 4*(col+1) + face_idx)
                
        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
        
    