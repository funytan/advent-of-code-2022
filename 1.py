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


            
with open('inputs/input_1_2.txt', 'r') as f:
    curr_sum = 0
    ls= []
    while True:
        try:
            inp = f.readline().strip()
            if inp == '':
                ls.append(curr_sum)
                curr_sum = 0
            else:
                curr_sum += int(inp)
        except:
            break
    print(sum(sorted(ls)[::-1][:3]))