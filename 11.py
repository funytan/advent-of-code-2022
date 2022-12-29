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


class monkey_class():
    def __init__(self):
        self.items = deque()
        self.operation = [None, None] # Op, val
        self.test = -1 # divisible
        self.test_true = None
        self.test_false = None
        self.num_inspect = 0
        

monkeys = []

def do_operation(op, old, val):
    if op == '+':
        return (old+val)%modulo
    if op == '*':
        if val is None:
            return (old*old)%modulo
        else:
            return old*val%modulo
        
    
with open('inputs/input_11.txt', 'r') as f:
    for _ in range(8):
        monkeys.append(monkey_class())
        monkey = monkeys[-1]
        for num in range(7):
            inp = f.readline().strip()
        # if not inp:
        #     break
            if num == 1:
                _, items = inp.split(': ')
                for item in items.split(', '):
                    item = int(item)
                    monkey.items.append(item)
            if num == 2:
                _, ops = inp.split(' = ')
                _, op, val = ops.split(' ')
                if val == 'old':
                    val = None
                else:
                    val = int(val)
                monkey.operation = [op, val]
            if num == 3:
                _, test = inp.split('by ')
                monkey.test = int(test)
            if num == 4:
                _, test_true = inp.split('monkey ')
                monkey.test_true = int(test_true)
            if num == 5:
                _, test_false = inp.split('monkey ')
                monkey.test_false = int(test_false)
    
    modulo = 1
    for monkey in monkeys:
        modulo *= monkey.test
    
    for round_num in range(10000):
        for monkey in monkeys:
            op, val = monkey.operation
            while monkey.items:
                item = monkey.items.popleft()
                new_val = do_operation(op, item, val)
                # print(item, new_val, op)
                if new_val % monkey.test == 0:
                    monkeys[monkey.test_true].items.append(new_val)
                else:
                    monkeys[monkey.test_false].items.append(new_val)
                monkey.num_inspect += 1
        # break
    inspections = []
    for monkey in monkeys:
        inspections.append(monkey.num_inspect)
    
    inspections = sorted(inspections)[::-1]
    print(inspections[0] * inspections[1])
                
            
    
    
    
    
    
    
    
    
    
    