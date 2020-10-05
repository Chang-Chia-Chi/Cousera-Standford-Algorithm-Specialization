import copy
import time
import random
from datetime import datetime
import sys
sys.path.append("C:/Users/USER/Desktop/Advance/Algorithm/algorithm/Graph")
from Graph_Class import Graph
import math

def min_cut(graph):
    n = len(graph.vertices)
    m = len(graph.edges)
    
    # 終止條件
    if n == 2:
        return m / 2
    
    g = copy.deepcopy(graph)
    random.seed(datetime.now())
    edge_index = random.randint(0, m - 1)
    g.merge_v(edge_index)
    cuts = min_cut(g)
    return cuts

# read mincut file and build a dictionary
file = open("min_cut.txt", "r")
lines = file.readlines()
graph_dict = {}
for line in lines:
    v_list = line.split()
    head = v_list.pop(0)
    graph_dict[head] = v_list

graph = Graph(graph_dict)
n = len(graph.vertices)
m = len(graph.edges)
cut = m

tstart = time.time()
for i in range(2500):
    new_min = min_cut(graph)
    if new_min < cut:
        cut = new_min
tend = time.time()
print(cut)
print(tend - tstart)


