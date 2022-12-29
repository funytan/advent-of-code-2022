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

monkeys = {}

@lru_cache(maxsize=None)
def dfs(monkey, val):
    if monkey == 'humn':
        return val
    if type(monkeys[monkey]) == int:
        return monkeys[monkey]
    else:
        m1 = dfs(monkeys[monkey][0], val)
        m2 = dfs(monkeys[monkey][2], val)
    return eval(f"m1 {monkeys[monkey][1]} m2")
    

with open('inputs/input_21.txt', 'r') as f:
    idx = 0
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        monkey, conn = inp.split(': ')
        conn = conn.split(' ')
        if len(conn) == 1:
            monkeys[monkey] = int(conn[0])
        else:
            monkeys[monkey] = conn
    def binary_search(l, h):
        print(l,h)
        m = (l+h)//2
        val_1 = dfs('pvgq', m)
        if val_1 > 80164970870816:
            return binary_search(m, h)
        elif val_1 < 80164970870816:
            return binary_search(l, m)
        else:
            return m
        
    ans = binary_search(1, 10000000000000)
    print(ans)