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

valve_dict = defaultdict(list)
flow_rate_dict = {}
maxi_dic = defaultdict(int)
times = 26
so_far_max = [0]

@lru_cache(maxsize=None)
def max_flow_contrib(valve,left, opened, so_far):
    if left <= 1:
        return 0
    curr_contrib = flow_rate_dict[valve] * (left-1)
    
    if valve in mapping_dict and 1<<mapping_dict[valve] & opened == 0:
        maxi = curr_contrib
        maxi_dic[1<<mapping_dict[valve] | opened] = max(maxi_dic[1<<mapping_dict[valve] | opened], so_far+maxi)
    else:
        maxi=0
        maxi_dic[opened] = max(maxi_dic[opened], so_far)
    
    for next_valve in valve_dict[valve]:
        maxi = max(max_flow_contrib(next_valve,left-1, opened, so_far), maxi)
        if valve in mapping_dict and 1<<mapping_dict[valve] & opened == 0:
            maxi = max(curr_contrib + max_flow_contrib(next_valve,left-2, 1<<mapping_dict[valve] | opened, so_far+curr_contrib), maxi)
    return maxi
        

with open('inputs/input_16.txt', 'r') as f:
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        valves = re.findall('[A-Z]{2}', inp)
        flow_rate = int(re.search('\d+', inp)[0])
        valve_dict[valves[0]] = valves[1:]
        flow_rate_dict[valves[0]] = flow_rate

    mapping_dict = {valve:idx for idx, valve in enumerate([valve for valve in flow_rate_dict if flow_rate_dict[valve]>0])}
    mem = {valve:{left:{} for left in range(times+1)} for valve in valve_dict}
    print(max_flow_contrib('AA',times, 0, 0))
    
    maxi_dic_keys = [key for key in maxi_dic]
    ans = 0
    for idx_1 in range(len(maxi_dic_keys)):
        for idx_2 in range(idx_1+1, len(maxi_dic_keys)):
            key_1 = maxi_dic_keys[idx_1]
            key_2 = maxi_dic_keys[idx_2]
            if key_1 & key_2 == 0:
                ans = max(maxi_dic[key_1] + maxi_dic[key_2], ans)

        
    print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    