import time
import sys
from collections import defaultdict

# compute optimal knapsack
def opt_K(idx, w, data, cal):
    # if zero item or zero capacity, return 0
    if idx == 0 or w == 0:
        return 0

    # if subproblem has been calculated, return the value 
    # from dict.
    if idx in cal and w in cal[idx]:
        return cal[idx][w]
    
    v_i, w_i = data[idx][0], data[idx][1]
    # if item weight is larger than current capacity,
    # the item is impossible to be packed so return A[i-1, w]
    if w_i > w:
        m_v = opt_K(idx-1, w, data, cal)
    # Dynamic Programming with recursion to divide bigger problems
    # into smaller subproblems
    else:         
        m_v = max(opt_K(idx-1, w, data, cal),
                  opt_K(idx-1, w-w_i, data, cal) + v_i)
    # memorized computed best value for a certain (i, w) pair 
    # to avoid redudant work
    cal[idx][w] = m_v
    return m_v

idx = 1
data = {}
with open("knapsack_big.txt", 'r') as file:
    lines = file.readlines()
    m_w, n = lines[0].split()
    m_w, n = int(m_w), int(n)
    for line in lines[1:]:
        v, w = line.split()
        data[idx] = (int(v), int(w))
        idx += 1

# dict to memorized calculated value
cal = defaultdict(dict)
t1 = time.time()
# Enlarge recursion depth limit
sys.setrecursionlimit(3000)
print(opt_K(n, m_w, data, cal))
t2 = time.time() - t1
print(t2)
