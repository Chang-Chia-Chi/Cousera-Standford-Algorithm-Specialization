# https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm

import math
import time
from copy import deepcopy
from collections import defaultdict
from bitmasks import bitmasks

def int2Locs(num:int):
    l_str = "{0:025b}".format(num)
    l_lst = list(l_str)
    l_lst.reverse()
    return (1<<i for i in range(25) if l_lst[i] == '1')

def distance(p1:tuple, p2:tuple):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

t1 = time.time()
with open("tsp.txt", 'r') as file:
    lines = file.readlines()
    coords = {}
    idx = 0
    for line in lines[1:]:
        x, y = line.split()
        x, y  = float(x), float(y)
        coords[1 << idx] = (x, y)
        idx += 1

num_locs = len(coords)

# 初始化 A[{k}, k]
prev = defaultdict(dict)
curr = defaultdict(dict)
for loc in coords.keys():
    if loc == 1:
        continue
    prev[loc][loc] = distance(coords[1], coords[loc])

for n in range(2, num_locs):
    for s in bitmasks(num_locs-1, n):
        # 因取組合時先不考慮 1 必須乘上 2 變回實際的數字
        s = s << 1
        # 利用 s 計算 set 中包含哪些地點
        locs = int2Locs(s)
        for loc in locs:
            # S - {j}
            s_loc = s - loc
            m_len = float('inf')
            # k = S - {j}
            t = int2Locs(s_loc)
            # DP
            for k in t:
                p1, p2 = coords[k], coords[loc]
                d = distance(p1, p2)
                if m_len > prev[s_loc][k] + d:
                    m_len = prev[s_loc][k] + d
            # 更新最新距離
            curr[s][loc] = m_len
    prev = curr
    curr = defaultdict(dict)

curr = prev
del prev

# 最短距離 = A[{1,2,...,n}, j] + Cj1
res = float('inf')
for _, m_len in curr.items():
    p1 = coords[1]
    for loc in m_len.keys():
        p2 = coords[loc]
        if res > m_len[loc] + distance(p1, p2):
            res = m_len[loc] + distance(p1, p2)

t2 = time.time() - t1
print(res, t2)
