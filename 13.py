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
    


idx = 1
ans = 1
dic = {}

def evaluate(item_1, item_2):
    # print('start', item_1, item_2)
    if type(item_1) == list and type(item_2) == int:
        item_2 = [item_2]
    if type(item_2) == list and type(item_1) == int:
        item_1 = [item_1]
    if type(item_1) == type(item_2) == int:
        if item_1 == item_2:
            return None
        elif item_1 < item_2:
            return True
        else:
            return False
    else:
        for idx, i1 in enumerate(item_1):
            if idx == len(item_2):
                return False
            check = evaluate(i1, item_2[idx])
            if check is not None:
                return check
        # print(len(item_1), len(item_2))
        if len(item_1) == len(item_2):
            return None
        elif len(item_1) < len(item_2):
            return True
        else:
            return False

packets = [[[2]], [[6]]]
with open('inputs/input_13.txt', 'r') as f:
    while True:
        inp_1 = f.readline().strip()
        if not inp_1:
            break
        inp_2 = f.readline().strip()
        f.readline().strip()
        inp_1 = deque(eval(inp_1))
        inp_2 = deque(eval(inp_2))
        packets.append(inp_1)
        packets.append(inp_2)
    
    
    for i, pac_i in enumerate(packets):
        order = 1
        for j, pac_j in enumerate(packets):
            if i == j:
                continue
            if not evaluate(pac_i, pac_j):
                order += 1
        if type(pac_i) == list and type(pac_i[0]) == list and len(pac_i[0]) == 1:
            if pac_i[0][0] == 2 or pac_i[0][0]== 6:
                print(order)
                ans*=order
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    