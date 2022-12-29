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

blueprint_costs = []

@lru_cache(maxsize=None)
def get_max_geodes(ore, clay, obs, ore_r, clay_r, obs_r, geo_r, min_left):
    # print(ore, clay, obs, ore_r, clay_r, obs_r, geo_r, min_left)
    if min_left == 0:
        return 0
    ans = 0
    # make ore robot
    if ore >= blueprint_costs[0] and ore_r <4:
        ans = max(get_max_geodes(
            ore + ore_r - blueprint_costs[0], 
            clay + clay_r, 
            obs + obs_r, 
            ore_r+1,
            clay_r, 
            obs_r, 
            geo_r, 
            min_left-1
            ), 
            ans
        )
    if ore >= blueprint_costs[1] and clay_r < blueprint_costs[2][1]:
        ans = max(get_max_geodes(
            ore + ore_r - blueprint_costs[1], 
            clay + clay_r, 
            obs + obs_r, 
            ore_r,
            clay_r+1, 
            obs_r, 
            geo_r, 
            min_left-1
            ), 
            ans
        )
    if ore >= blueprint_costs[2][0] and clay >= blueprint_costs[2][1] and obs_r < blueprint_costs[3][1]:
        ans = max(get_max_geodes(
            ore + ore_r - blueprint_costs[2][0], 
            clay + clay_r - blueprint_costs[2][1], 
            obs + obs_r, 
            ore_r,
            clay_r, 
            obs_r+1, 
            geo_r, 
            min_left-1
            ), 
            ans
        )
    if ore >= blueprint_costs[3][0] and obs >= blueprint_costs[3][1]:
        ans = max(get_max_geodes(
            ore + ore_r - blueprint_costs[3][0], 
            clay + clay_r, 
            obs + obs_r - blueprint_costs[3][1], 
            ore_r,
            clay_r, 
            obs_r, 
            geo_r+1, 
            min_left-1
            ), 
            ans
        )
    ans = max(get_max_geodes(
        ore + ore_r, 
        clay + clay_r, 
        obs + obs_r, 
        ore_r,
        clay_r, 
        obs_r, 
        geo_r, 
        min_left-1
        ), 
        ans
    )
    # if (ans + geo_r) == 1:
    #     print(ore, clay, obs, ore_r, clay_r, obs_r, geo_r, min_left)
    return ans + geo_r
    

    
blueprints = []

with open('inputs/input_19.txt', 'r') as f:
    while True:
        inp = f.readline().strip()
        if not inp:
            break
        costs = list(map(int, re.findall('\d+', inp)[1:]))
        blueprints.append([
            costs[0],
            costs[1],
            (costs[2], costs[3]),
            (costs[4], costs[5]) 
        ]
        )

res = 1
ans = []
for idx, blueprint in enumerate(blueprints,1):
    print(idx)
    blueprint_costs = blueprint
    here = get_max_geodes(0,0,0,1,0,0,0,32)
    ans.append(here)
    print(here)
    res *= here
    get_max_geodes.cache_clear()
                