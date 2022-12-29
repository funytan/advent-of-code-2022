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


with open('inputs/input_7_1.txt', 'r') as f:
    while True:
        curr_dic = levels[-1]
        inp = f.readline().strip()
        if not inp:
            break
        if inp[0] == '$':
            if inp.split(' ')[1] == 'cd':
                if inp.split(' ')[2] == '/':
                    levels = [levels[0]]
                elif inp.split(' ')[2] == '..':
                    levels.pop()
                else:
                    #  go to dir
                    direc = inp.split(' ')[2]
                    curr_dic = curr_dic['direcs'][direc]
                    levels.append(curr_dic)
        else:
            if inp.split(' ')[0] == 'dir':
                curr_dic['direcs'][inp.split(' ')[1]] = {'direcs':{}, 'files':{}}
            else:
                curr_dic['files'][inp.split(' ')[1]] = int(inp.split(' ')[0])

memory = []

def get_mem(dic):
    curr_mem = 0
    for direc in dic['direcs']:
        # if direc in memory:
        #     direc_mem = memory[direc]
        # else:
        direc_mem = get_mem(dic['direcs'][direc])
        curr_mem += direc_mem
    for file in dic['files']:
        curr_mem += dic['files'][file]     
    memory.append(curr_mem)
    return curr_mem

get_mem(levels[0])

total_mem = 0
for item in memory:
    if item <= 100000:
        total_mem += item
    
                    
                    
                    
        
    
        
        
        
        
        # seg_1, seg_2 = inp.split(',')
        # s1, e1 = list(map(int, seg_1.split('-')))
        # s2, e2 = list(map(int, seg_2.split('-')))
