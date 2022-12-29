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

final_ans = 0

with open('inputs/input_25.txt', 'r') as f:
    idx = 0
    while True:
        inp = f.readline()[:-1]
        if not inp:
            break
        ans = 0
        for idx, char in enumerate(inp):
            exp = len(inp) -1 - idx
            if '0' <= char <= '2':
                ans+= int(char) * 5**exp
            elif char == '=':
                ans -= 2*5**exp
            else:
                ans -= 5**exp
        # print(inp, 'inp')
        # print(ans)
        final_ans += ans
    # print(final_ans)

def base_5_rep(dec):
    exp = 0
    rep = ''
    while 5**exp <= dec:
        exp+=1
    exp -= 1
    for curr_exp in range(exp,-1,-1):
        num = 0
        while dec>=0:
            dec -= 5**curr_exp
            num+=1
        dec += 5**curr_exp
        num-=1
        rep += str(num)
    if not rep:
        return '0'
    else:
        return rep
                
        
rep = base_5_rep(final_ans)

snafu = ''
carry = False
for idx in range(len(rep)-1,-1,-1):
    char = rep[idx]
    if carry:
        digit = int(char) + 1
    else:
        digit = int(char)
    carry = False
    if digit == 3:
        snafu += '='
        carry = True
    elif digit == 4:
        snafu += '-'
        carry = True
    elif digit == 5:
        snafu += '0'
        carry = True
    else:
        snafu += str(digit)

if carry:
    snafu += '1'

        

print(snafu[::-1])


                    
                    
                    
                    
                    
                    
                    
                    
                    
                
        
    